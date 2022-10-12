import unittest

# change the import to test the different versions of is_valid_email
from is_valid_email import is_valid_email_3


class TestIsValidEmailUtil(unittest.TestCase):
    def test_rejects_wrong_argument_type(self):
        with self.assertRaisesRegex(TypeError, "email must be a string"):
            is_valid_email_3(5)

    def test_returns_true_for_valid_emails(self):
        emails = [
            "mustafa@najah.edu",
            "mustafa@najah.ac",
            "mustafa_assaf@najah.edu",
            "mustafa_assaf2@najah.ac",
        ]

        for email in emails:
            self.assertTrue(is_valid_email_3(email), f"{email} should be valid")

    def test_returns_false_for_invalid_emails(self):
        emails = [
            "mustafa_assaf@najah.com",
            "mustafa_assaf2@najahac",
            "mustafa&assaf@najah.edu",
            "mustafanajah.ac",
            "mustafanajah.ac",
            "5ustafa@najah.edu",
        ]

        for email in emails:
            self.assertFalse(is_valid_email_3(email), f"{email} should be invalid")


if __name__ == "__main__":
    unittest.main()
