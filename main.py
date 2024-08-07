import subprocess

def run_chatbot(model_path, user_input):
    """Runs the llamafile model with user input and returns the response.

    Args:
        model_path (str): Path to the llamafile model.
        user_input (str): User's message.

    Returns:
        str: The chatbot's response. 
    """

    process = subprocess.Popen(
        [model_path,  "-p",  user_input], 
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    stdout, stderr = process.communicate()

    # Basic error handling 
    if stderr:
        print(f"Error: {stderr}")
        return "An error occurred."

    return stdout.strip()  # Return only the relevant output

if __name__ == "__main__":
    model_path = "./TinyLlama-1.1B-Chat-v1.0.F16.llamafile" # Update if needed
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break
        response = run_chatbot(model_path, user_input)
        print(f"Chatbot: {response}")