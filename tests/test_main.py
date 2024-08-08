import unittest
from unittest.mock import patch
from io import StringIO
import sys
from main import process_user_input 

class TestMain(unittest.TestCase):

    def test_process_user_input_exit(self):
        """Test 'exit' command handling."""
        self.assertEqual(process_user_input("exit"), "Exiting...")
        self.assertEqual(process_user_input("EXIT"), "Exiting...")

    def test_process_user_input_message(self):
        """Test regular message processing."""
        self.assertEqual(process_user_input("Hello"), "Chatbot response (mocked)")

    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.input', side_effect=["Test instructions", "Hello", "exit"])
    def test_main_loop(self, mock_input, mock_stdout):
        """Test the main loop."""
        from main import __name__ as main_name
        with patch.object(main_name, "__name__", "__main__"):
            main_name.main()
        output = mock_stdout.getvalue()
        self.assertIn("Chatbot: Chatbot response (mocked)", output)
        self.assertIn("Chatbot: Exiting...", output)