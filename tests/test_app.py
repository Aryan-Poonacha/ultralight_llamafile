import unittest
from streamlit.testing.v1 import AppTest

class TestStreamlitApp(unittest.TestCase):

    def setUp(self):
        self.at = AppTest.from_file("app.py")

    def test_initialize_session_state(self):
        self.at.run()
        self.assertIn("messages", self.at.session_state)
        self.assertEqual(self.at.session_state["messages"], [])

    def test_display_chat_history(self):
        self.at.run()
        self.at.session_state["messages"] = [{"role": "user", "content": "Hello"}]
        self.at.run()
        # Ensure the chat history is displayed correctly
        chat_history_displayed = any("You: Hello" in element.value for element in self.at.markdown)
        self.assertTrue(chat_history_displayed, "Chat history may not be displayed correctly")

if __name__ == '__main__':
    unittest.main()
