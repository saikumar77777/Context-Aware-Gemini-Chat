import os
import google.generativeai as genai
from dotenv import load_dotenv

def get_valid_temperature():
    """Get a valid temperature value from the user."""
    while True:
        try:
            temp = float(input("Enter temperature (default 0.7): ").strip() or "0.7")
            if 0 <= temp <= 1:
                return temp
            print("Temperature must be between 0 and 1. Please try again.")
        except ValueError:
            print("Please enter a valid number between 0 and 1.")

def initialize_gemini(api_key, temperature=0.7):
    """Initialize the Gemini model with the given API key and temperature."""
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-1.5-flash',
                                generation_config=genai.types.GenerationConfig(
                                    temperature=temperature
                                ))
    return model

def get_user_input(prompt):
    """Get input from the user with the given prompt."""
    return input(prompt).strip()

def main():
    # Load environment variables
    load_dotenv(override=True)
    
    # Get API key from environment variable
    api_key = os.getenv('GOOGLE_API_KEY')
    if not api_key:
        print("Error: GOOGLE_API_KEY environment variable not found.")
        print("Please create a .env file with your API key: GOOGLE_API_KEY=your_api_key_here")
        return

    # Get temperature from user
    print("\nConfigure model parameters:")
    temperature = get_valid_temperature()

    # Initialize chat
    print("\nInitializing Gemini chat...")
    model = initialize_gemini(api_key, temperature)
    chat = model.start_chat(history=[])

    # First turn
    print("\nFirst turn:")
    first_input = get_user_input("Enter your first message: ")
    first_response = chat.send_message(first_input)
    print("\nGemini's response:")
    print(first_response.text)

    # Second turn
    print("\nSecond turn:")
    second_input = get_user_input("Enter your second message: ")
    second_response = chat.send_message(second_input)
    print("\nGemini's final response:")
    print(second_response.text)

    # Optional: Third turn
    print("\nWould you like to continue the conversation? (yes/no)")
    if get_user_input("").lower() == 'yes':
        third_input = get_user_input("Enter your third message: ")
        third_response = chat.send_message(third_input)
        print("\nGemini's final response:")
        print(third_response.text)

if __name__ == "__main__":
    main()