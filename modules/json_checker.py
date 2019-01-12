from typing import Dict, Tuple, List, Text

KEYS = [
    "name",
    "function",
    "phone",
    "email",
    "address",
    "portfolio",
    "education",
    "experience",
    "skills",
    "languages",
]


def check_json_keys(json: Dict) -> Tuple[bool, List[Text]]:
    """Check necessary keys to make resume."""
    missing_keys = list(filter(lambda key: key not in json.keys(), KEYS))
    return not any(missing_keys), missing_keys
