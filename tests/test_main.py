# tests/test_main.py
import unittest
from unittest.mock import patch
from io import StringIO
import sys

# Import the function to be tested
from main import run_chatbot

class TestMain(unittest.TestCase):

    @patch('sys.stdout', new_callable=StringIO)
    def test_run_chatbot_error(self, mock_stdout):
        """
        Test that run_chatbot gracefully handles exceptions. 
        We simulate an error by providing a wrong base_url.
        """
        # Call the function that prints to stdout
        run_chatbot("Hi", "You are a helpful AI assistant.")
        # Assert that the expected output was printed to stdout
        assert "An error occurred" in mock_stdout.getvalue()

    @patch('main.input', side_effect=["Custom instructions", "Hello", "exit"])
    @patch('main.run_chatbot', return_value="Mock chatbot response")
    @patch('sys.stdout', new_callable=StringIO)
    def test_main_loop(self, mock_stdout, mock_run_chatbot, mock_input):
        """Test the main loop with mocked input and chatbot response."""
        # Call the main function (which is executed when __name__ == "__main__")
        from main import __name__ as main_name 
        with patch.object(main_name, "__name__", "__main__"):
            main_name.main()
        # Assert that the loop interacted with the chatbot as expected
        mock_run_chatbot.assert_called_with("Hello", "Custom instructions") 
        # Assert that the loop printed the expected output
        assert "Chatbot: Mock chatbot response" in mock_stdout.getvalue()