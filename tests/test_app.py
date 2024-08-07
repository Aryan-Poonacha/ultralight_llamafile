import unittest
from unittest.mock import patch
import streamlit as st
from io import StringIO

# Assuming 'app' is the name of the file containing your Streamlit app code
import app

class TestApp(unittest.TestCase):

    @patch('app.openai.ChatCompletion.create')
    def test_run_chatbot_success(self, mock_create):
        """Tests the chatbot function with a successful response."""
        mock_create.return_value.choices = [type('obj', (object,), {'message': type('obj', (object,), {'content': 'This is a test response.'})})]

        # Simulate user input
        user_input = "Hello there!"
        
        # Call the function
        response = app.run_chatbot(user_input)

        # Assert the expected output
        self.assertEqual(response, "This is a test response.")
    
    @patch('app.openai.ChatCompletion.create')
    def test_run_chatbot_error(self, mock_create):
        """Tests the chatbot function when an error occurs."""
        mock_create.side_effect = Exception("Test Exception")

        # Simulate user input
        user_input = "Hello there!"
        
        # Call the function
        response = app.run_chatbot(user_input)

        # Assert the expected output
        self.assertEqual(response, "An error occurred: Test Exception")

if __name__ == '__main__':
    unittest.main()