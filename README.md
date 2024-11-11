# Thoughtful AI Customer Support Agent

This is a simple customer support AI agent for Thoughtful AI. It uses predefined responses for common questions about Thoughtful AI and falls back on an OpenAI LLM for other queries.

## Features
- Responds to predefined questions about Thoughtful AI agents.
- Fallbacks to OpenAI LLM for questions outside the predefined dataset.
- Simple UI built with Streamlit.

## Prerequisites

- Python 3.7 or higher
- [OpenAI API Key](https://platform.openai.com/signup) (needed for LLM fallback)

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/ZoraizDev/AI-Assistance.git
   cd chatbot

2. Install dependencies:
   ```bash
   pip install -r requirements.txt

4. Create a .env file in the project root and add your OpenAI API key:
   OPENAI_API_KEY=your_openai_api_key
## Running the App

1. Start the Streamlit app:
   ```bash
   streamlit run chat.py
2. Open your browser and go to http://localhost:8501 to interact with the AI agent.
