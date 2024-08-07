# main.py
#!/usr/bin/env python3
from openai import OpenAI

def run_chatbot(user_input):
    """Runs the chatbot, sending user input to the llamafile model and returning the response."""

    try:
        client = OpenAI(
            base_url="http://localhost:8080/v1",  
            api_key="sk-no-key-required" 
        )

        completion = client.chat.completions.create(
            model="LLaMA_CPP",
            messages=[
                {"role": "system", "content": "You are a helpful AI assistant."},
                {"role": "user", "content": user_input} 
            ]
        )
        return completion.choices[0].message.content 

    except Exception as e:
        print(f"An error occurred: {e}")
        return "An error occurred."

if __name__ == "__main__":
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break
        response = run_chatbot(user_input)
        print(f"Chatbot: {response}")