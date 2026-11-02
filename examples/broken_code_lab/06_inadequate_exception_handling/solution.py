import json

DEFAULTS = {"timeout_seconds": 30, "retries": 3}


class SettingsError(Exception):
    """The settings file exists but cannot be used."""


def _positive_int(settings, key, path):
    value = settings[key]
    if isinstance(value, bool) or not isinstance(value, int) or value < 1:
        raise SettingsError(f"{path}: '{key}' must be a positive integer, got {value!r}")


def load_settings(path):
    """Load settings from a JSON file and merge them over DEFAULTS.

    - A missing file is fine: use the defaults.
    - A file that exists but is not valid JSON, or not a JSON object, is a deployment error.
    - `timeout_seconds` and `retries` must be positive integers.
    """
    try:
        with open(path, encoding="utf-8") as handle:
            loaded = json.load(handle)
    except FileNotFoundError:
        return dict(DEFAULTS)
    except json.JSONDecodeError as exc:
        raise SettingsError(f"{path}: invalid JSON: {exc}") from exc
    # Other OSErrors (permissions, is-a-directory) propagate: they are not "no file".

    if not isinstance(loaded, dict):
        raise SettingsError(f"{path}: expected a JSON object, got {type(loaded).__name__}")

    settings = dict(DEFAULTS)
    settings.update(loaded)
    _positive_int(settings, "timeout_seconds", path)
    _positive_int(settings, "retries", path)
    return settings
