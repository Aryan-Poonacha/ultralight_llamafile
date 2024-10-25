#!/usr/bin/env python3
from openai import OpenAI
import mmap

def load_model_memory_mapped(model_path):
    """Loads a model using memory mapping."""
    # ... (implementation from previous response - remains the same)

def run_chatbot(user_input, port=8080, instructions="You are a helpful AI assistant.", model_path=None):
    """Runs the chatbot, potentially using a memory-mapped model."""
    try:
        client = OpenAI(
            base_url=f"http://localhost:{port}/v1",
            api_key="sk-no-key-required"
        )

        if model_path:
            mm = load_model_memory_mapped(model_path)
            if mm:
                try:
                    # Example (replace with your actual llama.cpp integration)
                    # model = llama.cpp.load_model_from_memory(mm) # Hypothetical function

                    completion = client.chat.completions.create(
                        model="LLaMA_CPP", # Correct model identifier
                        messages=[
                            {"role": "system", "content": instructions},
                            {"role": "user", "content": user_input}
                        ]
                    )
                finally:
                    mm.close() # Always close the mmap object in the finally block
        else:
            # ... (Existing logic without memory mapping - remains the same)
            completion = client.chat.completions.create( # Move this OUTSIDE the if block
                model="LLaMA_CPP",  # Correct model identifier here as well!
                messages=[
                    {"role": "system", "content": instructions},
                    {"role": "user", "content": user_input}
                ]
            )

        return completion.choices[0].message.content  # This should be outside the if/else

    except Exception as e:  # Handle all exceptions here
        print(f"An error occurred: {e}")
        return "An error occurred."

def process_user_input(user_input):
    """
    Processes user input, handling 'exit' and returning a response.
    This function can be unit tested as it doesn't directly call 
    the external API.
    """
    if user_input.lower() == "exit":
        return "Exiting..."
    else:
        return user_input

def process_user_input_test(user_input):
    """
    Processes user input, handling 'exit' and returning a response.
    This function can be unit tested as it doesn't directly call 
    the external API.
    """
    if user_input.lower() == "exit":
        return "Exiting..."
    else:
        # In a real application, you would call run_chatbot here, 
        # but we'll return a placeholder for testing.
        return "Chatbot response (mocked)" 

if __name__ == "__main__":
    instructions = input("Enter custom system instructions(blank for default):")
    if not instructions:
        instructions = "You are a helpful AI assistant."

    while True:
        port = input("Enter port no of local server to use (default is 8080):")
        if not port:
            port = 8080
        else:
            try:
                port = int(port)
            except ValueError:
                print("Invalid port number. Please enter a valid integer.")
                continue

        user_input = input("You: ")
        processed_user_input = process_user_input(user_input)
        response = run_chatbot(processed_user_input, port, instructions)
        print(f"Chatbot: {response}")
        if response == "Exiting...":
            break
