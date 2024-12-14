from flask import Blueprint, render_template, request, jsonify
import json
import rhinoinside
rhinoinside.load()
import Rhino
import scriptcontext
import os
from datetime import datetime

views = Blueprint(__name__, "views")

votes = {}

VOTE_FILE='output/votes.json'

# Ensure the vote file exists, if not create it with an empty list
if not os.path.exists(VOTE_FILE):
    with open(VOTE_FILE, 'w') as file:
        json.dump([], file)  # Initialize the file with an empty list

@views.route("/")
def home():
		return render_template("index.html")

@views.route('/vote', methods=['POST'])
def vote():
    # Get the image number from the request (this comes from the JavaScript fetch request)
    data = request.get_json()  # Parse the JSON data sent from the client
    image_number = data.get('imageNumber')

    if image_number:
        # Read the current votes from the JSON file
        with open(VOTE_FILE, 'r') as file:
            votes = json.load(file)

        # Create a new vote entry
        new_vote = {
            'imageNumber': image_number,
            'voteTime': datetime.now().isoformat()  # Store the time of the vote
        }

        # Append the new vote to the list
        votes.append(new_vote)

        # Write the updated votes back to the file
        with open(VOTE_FILE, 'w') as file:
            json.dump(votes, file, indent=4)

        return jsonify({'status': 'success', 'message': f'You voted for Image {image_number}!'})

    else:
        return jsonify({'status': 'error', 'message': 'Invalid vote data!'})