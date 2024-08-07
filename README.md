# Basic Llamafile Chatbot 

[![CI/CD](https://img.shields.io/github/workflow/status/YOUR_USERNAME/YOUR_REPO_NAME/Build%20and%20Test)](https://github.com/YOUR_USERNAME/YOUR_REPO_NAME/actions)
[![Demo Video](LINK_TO_YOUR_DEMO_VIDEO)](LINK_TO_YOUR_DEMO_VIDEO)

This is a minimal chatbot application that demonstrates how to use a `llamafile` model to create a simple conversational agent.

## Architecture

This project utilizes a simple architecture:

- **`main.py`:** Contains the core logic to run the chatbot, interacting with the llamafile model.
- **`TinyLlama-1.1B-Chat-v1.0.F16.llamafile`:** (Not included in the repository) The pre-trained language model used by the chatbot.
- **Docker:** The application is packaged into a Docker container for easy deployment.

## Github Actions

Things included are:

* `Makefile`

* `Pytest`

* `pandas`

* `Ruff`:  

Run `make lint` which runs `ruff check`.  You can find out more info on [Ruff here](https://github.com/astral-sh/ruff).

* `Dockerfile`

* `GitHub copilot`

* `jupyter` and `ipython` 

## Setup and Running

1. **Prerequisites:**
   - Install [Docker](https://docs.docker.com/get-docker/).
   - Download the `TinyLlama-1.1B-Chat-v1.0.F16.llamafile` model from [https://github.com/Mozilla-Ocho/llamafile#other-example-llamafiles](https://github.com/Mozilla-Ocho/llamafile#other-example-llamafiles) and place it in the root of the project directory.

2. **Run Locally:**
   - Navigate to the project directory in your terminal.
   - Run `python main.py`.
   - Start chatting!

3. **Run with Docker:**
   - Build the image: `docker build -t my-chatbot .`
   - Run the container (replace `MODEL_PATH` with the correct path within the container, if necessary): 
      ```bash
      docker run -it --rm \
        -v $(pwd)/TinyLlama-1.1B-Chat-v1.0.F16.llamafile:/app/TinyLlama-1.1B-Chat-v1.0.F16.llamafile  \ 
        my-chatbot 
      ```

## Testing

Run unit tests: `python -m unittest test_main.py`

## Examples

**Input:** Hello there!
**Output:** Hi! How can I help you today?

## Performance/Evaluation 

(Add any performance observations or benchmarks here. For a simple project like this, focus on qualitative aspects like response time and coherence).

## Future Improvements

- Implement a more sophisticated chatbot interface (web UI, command-line arguments).
- Incorporate error handling and edge-case management.
- Explore more advanced functionalities of the `llamafile` model.
Based on the python ruff template provided. Created for IDS 706, Fall 2023.

## References

Gospel:

![1 1-function-essence-of-programming](https://github.com/nogibjj/python-ruff-template/assets/58792/f7f33cd3-cff5-4014-98ea-09b6a29c7557)



