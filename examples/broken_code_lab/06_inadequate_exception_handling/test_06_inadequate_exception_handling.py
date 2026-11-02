import json
import os

import pytest


def write(tmp_path, text):
    path = tmp_path / "settings.json"
    path.write_text(text, encoding="utf-8")
    return str(path)


def test_missing_file_uses_the_defaults(target, tmp_path):
    assert target.load_settings(str(tmp_path / "nope.json")) == {"timeout_seconds": 30, "retries": 3}


def test_file_values_override_the_defaults(target, tmp_path):
    path = write(tmp_path, json.dumps({"retries": 5}))
    assert target.load_settings(path) == {"timeout_seconds": 30, "retries": 5}


def test_corrupt_json_is_reported_not_hidden(target, tmp_path):
    path = write(tmp_path, '{"retries": ')
    with pytest.raises(target.SettingsError, match="invalid JSON") as info:
        target.load_settings(path)
    assert path in str(info.value)
    assert isinstance(info.value.__cause__, json.JSONDecodeError)


@pytest.mark.parametrize("text", ["[1, 2]", '"text"', "42", "null"])
def test_non_object_json_is_rejected(target, tmp_path, text):
    with pytest.raises(target.SettingsError, match="JSON object"):
        target.load_settings(write(tmp_path, text))


@pytest.mark.parametrize("key,value", [("retries", 0), ("retries", -1), ("timeout_seconds", "30"), ("timeout_seconds", True)])
def test_invalid_values_name_the_key(target, tmp_path, key, value):
    with pytest.raises(target.SettingsError, match=key):
        target.load_settings(write(tmp_path, json.dumps({key: value})))


def test_a_directory_is_not_mistaken_for_a_missing_file(target, tmp_path):
    with pytest.raises(OSError):
        target.load_settings(str(tmp_path))  # a directory: IsADirectoryError / PermissionError


@pytest.mark.skipif(os.name == "nt", reason="POSIX permissions")
def test_unreadable_file_is_not_silently_replaced_by_defaults(target, tmp_path):
    path = write(tmp_path, json.dumps({"retries": 5}))
    os.chmod(path, 0)
    try:
        if os.access(path, os.R_OK):
            pytest.skip("running as a user that ignores file permissions")
        with pytest.raises(PermissionError):
            target.load_settings(path)
    finally:
        os.chmod(path, 0o600)
