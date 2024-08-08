# tests/test_main.py
import unittest
from main import process_user_input, process_user_input_test

class TestMainFunctions(unittest.TestCase):

    def test_process_user_input_exit(self):
        self.assertEqual(process_user_input("exit"), "Exiting...")

    def test_process_user_input_non_exit(self):
        self.assertEqual(process_user_input("hello"), "hello")

    def test_process_user_input_test_exit(self):
        self.assertEqual(process_user_input_test("exit"), "Exiting...")

    def test_process_user_input_test_non_exit(self):
        self.assertEqual(process_user_input_test("hello"), "Chatbot response (mocked)")

if __name__ == '__main__':
    unittest.main()
