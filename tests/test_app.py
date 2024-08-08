# tests/test_app.py
import unittest
from streamlit.testing.v1 import AppTest

class TestStreamlitApp(unittest.TestCase):

    def setUp(self):
        self.at = AppTest.from_file("app.py")

    def test_initialize_session_state(self):
        self.at.run()
        self.assertIn("messages", self.at.session_state)
        self.assertEqual(self.at.session_state["messages"], [])

    def test_add_message(self):
        self.at.run()
        self.at.text_input("You: ").input("Hello").run()
        self.assertEqual(self.at.session_state["messages"], [{"role": "user", "content": "Hello"}])

    def test_display_chat_history(self):
        self.at.run()
        self.at.session_state["messages"] = [{"role": "user", "content": "Hello"}]
        self.at.run()
        self.assertIn("You: Hello", self.at.markdown[0].value)

if __name__ == '__main__':
    unittest.main()
