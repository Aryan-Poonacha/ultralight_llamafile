import unittest
from unittest.mock import patch, MagicMock
from app import initialize_session_state, add_message, display_chat_history 

class TestApp(unittest.TestCase):

    def setUp(self):
        """Set up for test methods."""
        self.patcher = patch('app.st') 
        self.mock_st = self.patcher.start()
        # Simulate an empty session state
        self.mock_st.session_state = {} 

    def tearDown(self):
        """Clean up after test methods."""
        self.patcher.stop()

    def test_initialize_session_state(self):
        """Test session state initialization."""
        initialize_session_state()
        self.assertEqual(self.mock_st.session_state.get("messages"), [])

    def test_add_message(self):
        """Test adding messages to session state."""
        initialize_session_state()  # Ensure messages list exists
        add_message("user", "Hello")
        add_message("assistant", "Hi there!")
        self.assertEqual(len(self.mock_st.session_state["messages"]), 2)
        self.assertEqual(self.mock_st.session_state["messages"][0]["content"], "Hello") 

    def test_display_chat_history(self):
        """Test displaying chat history. 
        We'll just check if the Streamlit functions are called
        with the expected arguments. 
        """
        self.mock_st.session_state.messages = [
            {"role": "user", "content": "Test message 1"},
            {"role": "assistant", "content": "Test response 1"}
        ]
        display_chat_history() 

        # Assert that st.write and st.markdown were called with the correct arguments
        self.mock_st.write.assert_called_with("You: Test message 1")
        self.mock_st.markdown.assert_called_with(
            "Chatbot: Test response 1", unsafe_allow_html=True
        )