import requests
import json
from dotenv import load_dotenv
import os

# Load environment variables from a .env file
load_dotenv()

# Set the Synthesia API key
synthesia_api_key = os.getenv("SYNTHESIA_API_KEY")

# Define the Synthesia API URL
synthesia_api_url = "https://api.synthesia.io/v2/videos"

# Define the payload for the Synthesia API
payload = {
    "script": {
        "input": "my name is hiba"
    },
    "title": "AI Avatar",
    "test": True,
    "avatar": "anna_costume1_cameraA",  # Replace with your Synthesia avatar ID
    "language": "en-US",  # Specify the language code
    "background": "green_screen"
}

# Define the headers for the Synthesia API
headers = {
    "Authorization": "a3a7f20e6e8aa1fd72d299c4f2559e7a",
    "accept": "application/json"
}

# Send the request to the Synthesia API
synthesia_response = requests.post(synthesia_api_url, headers=headers, data=json.dumps(payload))

# Check the response from the Synthesia API
if synthesia_response.status_code == 200:
    video_data = synthesia_response.json()
    video_url = video_data.get("video_url")
    print(f"Video created successfully! You can view it at: {video_url}")
else:
    print(f"Failed to create video. Status code: {synthesia_response.status_code}, Response: {synthesia_response.text}")
