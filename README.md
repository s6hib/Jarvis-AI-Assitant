# Jarvis: Your Friendly AI Terminal Assistant

Welcome to Jarvis, a friendly AI that helps you with your terminal commands. With Jarvis, you don't need to remember complex commands or keep Googling them. Simply ask Jarvis and it'll give you the command you need!

## Prerequisites
* Python 3.7 or later
* OpenAI's GPT-3.5-turbo or similar
* `openai` and `rich` Python libraries

## Setup
1. Clone this repository:
    ```bash
    git clone https://github.com/s6hib/Jarvis-AI-Assitant.git
    ```
2. Navigate to the directory:
    ```bash
    cd Jarvis-AI-Assitant
    ```
3. Install the required Python libraries:
    ```bash
    pip install openai rich
    ```
4. Set up your OpenAI API key. You can either set it directly in the script or via an environment variable.

## Usage
To use Jarvis, simply run the script with your query. Here's an example:
```bash
python main.py "how to create a directory named hello"
```
Jarvis will give you the command and ask for your permission to execute it.

## Limitations
Please note that due to the nature of subprocesses in Python, commands like `cd` won't persist across different executions of the script.
