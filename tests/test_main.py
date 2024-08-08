# tests/test_main.py
import unittest
from unittest.mock import patch
from io import StringIO
import sys

# Import the functions to be tested
from main import run_chatbot, main 

class TestMain(unittest.TestCase):

    @patch('sys.stdout', new_callable=StringIO)
    def test_run_chatbot_error(self, mock_stdout):
        """Test that run_chatbot gracefully handles exceptions."""
        run_chatbot("Hi", "You are a helpful AI assistant.")
        assert "An error occurred" in mock_stdout.getvalue()

    @patch('builtins.input', side_effect=["Custom instructions", "Hello", "exit"]) 
    @patch('main.run_chatbot', return_value="Mock chatbot response")
    @patch('sys.stdout', new_callable=StringIO)
    def test_main_loop(self, mock_stdout, mock_run_chatbot, mock_input):
        """Test the main loop with mocked input and chatbot response."""
        main()  # Directly call the main function
        mock_run_chatbot.assert_called_with("Hello", "Custom instructions")
        assert "Chatbot: Mock chatbot response" in mock_stdout.getvalue()