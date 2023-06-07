from rich.console import Console
from rich.theme import Theme
import openai
import os
import subprocess
import sys

# Set OpenAI API key
openai.api_key = os.getenv('OPENAI_API_KEY')

# Set up console with new theme for different colors
custom_theme = Theme({
  "ask": "yellow",
  "command": "bold magenta",
  "yes": "bold green",
  "no": "bold red",
  "running": "italic green",
  "cancelled": "bold red",
})
console = Console(theme=custom_theme)


# Function to request command from OpenAI
def request_command_from_openai(task: str) -> str:
  conversation_prompt = f"""
    You are Jarvis, my AI companion. Execute a shell command based on my instructions.  Provide only the command(s) needed for my request, else this won't work. Nothing but the executable command.

    Task: {task}
    """

  response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[{
      "role": "system",
      "content": conversation_prompt
    }],
    temperature=0.7,
  )

  # Extract and return the command from the OpenAI response
  return response.choices[0].message.content.strip()


# Main function
def run_assistant():
  # Gather all arguments as a single query string
  query = ' '.join(sys.argv[1:])

  # Fetch command from OpenAI
  shell_command = request_command_from_openai(query)

  # Write command to script file
  with open('run_me.sh', 'w') as file:
    file.write("#!/usr/bin/env bash\n")
    file.write(shell_command + "\n")

  # Display command to user and ask for permission to run it
  console.print(
    f"Ready to run this command: [command]{shell_command}[/command]")
  console.print("Press [yes]y[/yes] to execute, [no]n[/no] to cancel.",
                end=" ")

  # Wait for user input
  user_choice = input()

  # Run the command if user consents
  if user_choice.lower() == 'y':
    console.print("[running]Executing command...[/running]")
    subprocess.run(['bash', 'run_me.sh'])
  else:
    console.print("[cancelled]Command execution cancelled.[/cancelled]")


# Run the assistant when script is called
if __name__ == '__main__':
  run_assistant()
