import requests
import uuid
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("ELEVEN_API_KEY")

def generate_tts(text):
    url = "https://api.elevenlabs.io/v1/text-to-speech/pNInz6obpgDQGcFmaJgB"

    headers = {
        "xi-api-key": API_KEY,
        "Content-Type": "application/json"
    }

    data = {
        "text": text,
        "model_id": "eleven_multilingual_v2",
        "voice_settings": {
            "stability": 0.5,
            "similarity_boost": 0.8
        }
    }

    response = requests.post(url, json=data, headers=headers)

    output_path = f"output_{uuid.uuid4()}.mp3"

    with open(output_path, "wb") as f:
        f.write(response.content)

    return output_path