import os
from django.test import TestCase
from django.contrib.auth.password_validation import validate_password
class ConfigTest(TestCase):
    def test_secret_key_strength(self):
        secretKey = os.environ.get("DJANGO_SECRET_KEY")
        try:
            isStrong = validate_password(secretKey)
        except Exception as e:
            msg = f'Bad Secret key, {e.messages}'
            self.fail(msg)
        