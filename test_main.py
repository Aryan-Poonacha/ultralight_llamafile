      
from main import run_chatbot

def test_run_chatbot():
    """Tests the chatbot with a simple input."""

    model_path = "./TinyLlama-1.1B-Chat-v1.0.F16.llamafile"  # Update if needed
    user_input = "Hello there!"
    response = run_chatbot(model_path, user_input)
    assert isinstance(response, str), "Response should be a string."
    assert response != "An error occurred.", "Chatbot encountered an error."

    