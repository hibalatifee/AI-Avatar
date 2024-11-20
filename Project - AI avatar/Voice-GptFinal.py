import requests
import json
from dotenv import load_dotenv
import os

# Load environment variables from a .env file
load_dotenv()

# Set the Synthesia API key
synthesia_api_key = os.getenv("SYNTHESIA_API_KEY")

