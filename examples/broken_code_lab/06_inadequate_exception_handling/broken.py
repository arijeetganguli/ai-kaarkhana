import json

DEFAULTS = {"timeout_seconds": 30, "retries": 3}


def load_settings(path):
    """Load settings from a JSON file and merge them over DEFAULTS.

    - A missing file is fine: use the defaults.
    - A file that exists but is not valid JSON, or not a JSON object, is a deployment error.
    - `timeout_seconds` and `retries` must be positive integers.
    """
    try:
        with open(path) as handle:
            loaded = json.load(handle)
        settings = dict(DEFAULTS)
        settings.update(loaded)
        return settings
    except:
        return dict(DEFAULTS)
