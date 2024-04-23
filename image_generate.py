import requests, os
from dotenv import load_dotenv

load_dotenv()


API_URL = "https://api-inference.huggingface.co/models/Salesforce/blip-image-captioning-large"
BEAR_TOKEN = str(os.getenv("BEAR_TOKEN"))
headers = {"Authorization": f"Bearer {BEAR_TOKEN}"}

def query(filename):
    with open(filename, "rb") as f:
        data = f.read()
    response = requests.post(API_URL, headers=headers, data=data)
    return response.json()

