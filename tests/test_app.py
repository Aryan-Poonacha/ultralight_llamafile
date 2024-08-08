# tests/test_app.py
import unittest
from unittest.mock import patch

from app import run_chatbot 

class TestApp(unittest.TestCase): 

    @patch('app.OpenAI')
    def test_run_chatbot_error(self, mock_openai):
        """Test that run_chatbot gracefully handles exceptions."""
        mock_openai.side_effect = Exception("Simulated API error")
        result = run_chatbot("Hello")
        assert "An error occurred: Simulated API error" in result

    @patch('app.OpenAI')
    def test_run_chatbot_success(self, mock_openai):
        """Test that run_chatbot processes input and returns a response."""
        mock_client = mock_openai.return_value
        mock_client.chat.completions.create.return_value.choices[0].message.content = "Mock response"

        result = run_chatbot("Hello")
        assert "Mock response" in result