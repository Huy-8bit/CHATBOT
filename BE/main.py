# # import tkinter as tk

from flask import Flask, request, jsonify
from flask_cors import CORS

import import_data
import get_message


def get_text(input_text):
    # some code here to process the input text and generate output
    return get_message.get_messge(input_text)


app = Flask(__name__)
CORS(app)


@app.route('/send-message', methods=['POST'])
def send_message():
    # Get the message from the request body
    message = request.get_json()['input']
    message = message.lstrip()
    print("user:", message)
    # Process the message and get a response
    response = process_message(message)
    print("bot:", response)
    # Return the response as a JSON object
    return jsonify({'output': response})


def process_message(message):
    # Write code to process the message and generate a response
    response = get_text(message)
    return response


if __name__ == '__main__':
    app.run()
