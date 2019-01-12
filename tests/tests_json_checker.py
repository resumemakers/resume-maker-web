from unittest import TestCase
from modules.json_checker import check_json_keys, KEYS


class TestCheckJsonKeys(TestCase):
    def test_check_json_keys_should_return_tuples_with_bool_and_list(self):
        boolean, missing_keys = check_json_keys({'abc': 123})

        self.assertIsInstance(boolean, bool)
        self.assertIsInstance(missing_keys, list)

    def test_check_json_keys_should_return_false_when_key_missing(self):
        boolean, missing_keys = check_json_keys({'abc': 123})

        self.assertEqual(boolean, False)

    def test_check_json_keys_should_return_missing_keys(self):
        boolean, missing_keys = check_json_keys({'abc': 123})

        self.assertEqual(KEYS, missing_keys)

    def test_check_json_keys_should_return_only_name_key_name(self):
        json = {key: 1 for key in KEYS}
        json.pop('name')

        boolean, missing_keys = check_json_keys(json)

        self.assertIn('name', missing_keys)

    def test_check_json_keys_should_return_true_and_empty_list_when_recive_all_keys(self):
        json = {key: 1 for key in KEYS}

        boolean, missing_keys = check_json_keys(json)

        self.assertEqual(True, boolean)
        self.assertEqual([], missing_keys)
