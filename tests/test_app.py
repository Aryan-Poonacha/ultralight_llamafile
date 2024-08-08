# tests/test_app.py
import unittest
from unittest.mock import patch
import streamlit as st
from app import initialize_session_state, add_message, display_chat_history

class TestStreamlitApp(unittest.TestCase):

    @patch('streamlit.session_state', {})
    def test_initialize_session_state(self):
        initialize_session_state()
        self.assertIn("messages", st.session_state)
        self.assertEqual(st.session_state.messages, [])

    @patch('streamlit.session_state', {"messages": []})
    def test_add_message(self):
        add_message("user", "Hello")
        self.assertEqual(st.session_state.messages, [{"role": "user", "content": "Hello"}])

    @patch('streamlit.session_state', {"messages": [{"role": "user", "content": "Hello"}]})
    @patch('streamlit.write')
    @patch('streamlit.markdown')
    def test_display_chat_history(self, mock_markdown, mock_write):
        display_chat_history()
        mock_write.assert_called_with("You: Hello")

if __name__ == '__main__':
    unittest.main()