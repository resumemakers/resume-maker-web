from unittest import TestCase
from flask import url_for
from resumemaker import app


class BaseTestCase(TestCase):
    def setUp(self):
        """Create client base TestCase."""
        self.app = app
        self.app.config['SERVER_NAME'] = 'localhost:5000'
        self.app_context = self.app.test_request_context()
        self.app_context.push()
        self.client = self.app.test_client()
        self.app.testing = True


class ApiTests(BaseTestCase):
    def test_make_resume(self):
        ...
