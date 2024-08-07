import unittest
from unittest.mock import patch
from io import StringIO
import main 

class TestChatbot(unittest.TestCase):

    @patch('sys.stdout', new_callable=StringIO)
    def test_run_chatbot_success(self, mock_stdout):
        # Test a successful chatbot interaction
        with patch('main.openai.ChatCompletion.create') as mock_create:
            mock_create.return_value.choices = [type('obj', (object,), {'message': type('obj', (object,), {'content': 'This is a test response.'})})]
            main.run_chatbot("Test input")
            self.assertEqual(mock_stdout.getvalue().strip(), "Chatbot: This is a test response.")

    @patch('sys.stdout', new_callable=StringIO)
    def test_run_chatbot_error(self, mock_stdout):
        # Test error handling in the chatbot
        with patch('main.openai.ChatCompletion.create') as mock_create:
            mock_create.side_effect = Exception("Test Exception")
            main.run_chatbot("Test input")
            self.assertEqual(mock_stdout.getvalue().strip(), "Chatbot: An error occurred.")

if __name__ == '__main__':
    unittest.main()