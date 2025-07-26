# Project 2: Text Summarizer Agent
This project will create an AI agent that takes a piece of text as input and provides a concise summary.

Step 1: Project Setup
Create a New Project Directory:
Open your terminal and create a new folder for this project.

Bash

mkdir summarizer_agent_project
cd summarizer_agent_project
Create a Virtual Environment:
It's good practice to create a new virtual environment for each project to manage dependencies.

Bash

python3 -m venv .venv
Activate the Virtual Environment:

Bash

source .venv/bin/activate
(You should see (.venv) or (summarizer_agent_project) at the beginning of your terminal prompt, indicating the virtual environment is active.)

Install Required Libraries:

Bash

pip install python-dotenv google-generativeai openai agents-ai
python-dotenv: To load environment variables.

google-generativeai: Google's official client for Gemini (though agents-ai abstracts it, it's good to have).

openai: The agents-ai library uses an AsyncOpenAI client that is compatible with the OpenAI API, which Gemini's "OpenAI endpoint" emulates.

agents-ai: The core library for building agents.

Create .env file:
In the summarizer_agent_project directory, create a file named .env and add your Gemini API key:

GEMINI_API_KEY="YOUR_GEMINI_API_KEY_HERE"
Important: Replace "YOUR_GEMINI_API_KEY_HERE" with your actual Gemini API Key. Keep this file private and never commit it to public repositories.

Step 2: Create connection.py
This file will handle the connection setup to the Gemini API, similar to your previous project.

Create connection.py:
In your summarizer_agent_project directory, create a file named connection.py and paste the following code:

# summarizer_agent_project
