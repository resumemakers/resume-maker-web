from itertools import filterfalse
from typing import Dict, Tuple, List, Text

KEYS = {
    "name": str,
    "function": str,
    "phone": str,
    "email": str,
    "address": str,
    "portfolio": str,
    "education": Dict,
    "experience": Dict,
    "skills": Dict,
    "languages": Dict,
}


def check_json_keys(
    json: Dict, *, keys: Dict = KEYS
) -> Tuple[bool, List[Text]]:
    """Check necessary keys to make resume."""
    missing_keys = list(filter(lambda key: key not in json.keys(), KEYS))
    return not any(missing_keys), missing_keys


def check_json_types(
    json: Dict, *, keys: Dict = KEYS
) -> Tuple[bool, List[Text]]:
    """Check necessary keys to make resume."""
    missing_keys = list(
        filterfalse(lambda key: isinstance(json[key], KEYS[key]), KEYS)
    )
    return not any(missing_keys), missing_keys
