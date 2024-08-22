import openai
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

# Set your OpenAI API key
openai.api_key = 'your_openai_api_key'

@app.route("/", methods=["POST"])
def bot():
    # User input
    user_msg = request.values.get('Body', '').lower()

    # Creating object of MessagingResponse
    response = MessagingResponse()

    # Query ChatGPT API
    chatgpt_response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=user_msg,
        max_tokens=150
    )

    # Extract the response text
    answer = chatgpt_response.choices[0].text.strip()

    # Displaying result
    msg = response.message(f"--- Response for '{user_msg}' ---\n{answer}")

    return str(response)

if __name__ == "__main__":
    app.run()
