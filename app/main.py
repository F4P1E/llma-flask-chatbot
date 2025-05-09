from flask import Flask, request, jsonify  # Import necessary Flask modules for creating the web app
from model import generate_response  # Import the function to generate AI responses
from dotenv import load_dotenv  # Import dotenv to load environment variables
from prompts  # This line seems incomplete and will cause an error
import os  # Import os for environment variable handling

# Load environment variables from a .env file
load_dotenv()

# Initialize the Flask application
app = Flask(__name__)

# Define a route for the chatbot API
@app.route('/chat', methods=['POST'])
def chat():
    # Get JSON data from the POST request
    data = request.get_json()
    # Extract the 'prompt' field from the JSON data
    prompt = data.get('prompt', '')

    # Define the system prompt for the AI model
    system_prompt = (
        "You are a friendly and supportive AI coach for digital wellness. "
        "Give thoughtful responses about screen time, stress, and emotional balance.\n"
    )
    # Construct the full prompt for the AI model
    full_prompt = f"{SYSTEM_PROMPT}User: {user_input}\nAI:"
    # Generate a response using the AI model
    response = generate_response(full_prompt)

    # Return the AI response as a JSON object
    return jsonify({'response': response})

# Run the Flask application on host 0.0.0.0 and port 5000
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
