# Gemini Console Chatbot

This project is a simple **console-based chatbot** that uses Google's Gemini API to have multi-turn conversations, preserving context between turns. It is designed for use in the terminal/command prompt only—no web or GUI interface is used.

## What the Script Does
- Prompts the user for input in the console
- Sends each message to the Gemini model (Google's generative AI)
- Maintains conversation context across multiple turns, so the model "remembers" earlier messages
- Prints the model's response to the console after each turn
- Allows you to optionally continue the conversation for a third turn

## Setup & Dependencies

1. **Clone or download this repository** to your local machine.
2. **Install dependencies** using pip:
   ```bash
   pip install -r requirements.txt
   ```
3. **Get a Google Gemini API key** from [Google AI Studio](https://makersuite.google.com/app/apikey).
4. **Create a `.env` file** in the project directory (same folder as `gemini_chat.py`) and add your API key:
   ```
   GOOGLE_API_KEY=your_actual_api_key_here
   ```
   - Make sure there are no spaces or quotes around the key.
   - The variable name must be exactly `GOOGLE_API_KEY`.

## How to Run

1. Open a terminal or command prompt in the project directory.
2. Run the chatbot script:
   ```bash
   python gemini_chat.py
   ```
3. Follow the prompts in the console to chat with Gemini.

## Notes
- This script is **console-only**—no Streamlit or web interface is used.
- The conversation context is preserved for a natural, multi-turn chat experience.
- If you see an error about the API key, double-check your `.env` file and its location.

## Requirements
- Python 3.7+
- `google-generativeai` Python package
- `python-dotenv` Python package

All dependencies are listed in `requirements.txt`. 