from django.test import TestCase


class BasicTestCase(TestCase):

    def test_check_correct_result(self):
        self.assertEqual(2+2, 4)

    def test_check_incorrect_result(self):
        self.assertNotEqual(1+2, 4)
