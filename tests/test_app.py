# tests/test_app.py
import unittest
from unittest.mock import patch
import streamlit as st

# Import the function to be tested
from app import run_chatbot

def test_run_chatbot_error():
    """Test that run_chatbot gracefully handles exceptions."""
    with patch('app.OpenAI') as mock_openai:
        # Configure the mock to raise an exception
        mock_openai.side_effect = Exception("Simulated API error")
        # Call the function and assert it handles the exception
        result = run_chatbot("Hello")
        assert "An error occurred: Simulated API error" in result