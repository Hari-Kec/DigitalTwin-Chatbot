from openai import OpenAI
import requests
import uuid
from config import OPENAI_API_KEY, ELEVENLABS_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)

def generate_response(prompt, persona_style):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": persona_style},
            {"role": "user", "content": prompt}
        ],
        temperature=0.8
    )
    return response.choices[0].message.content

def synthesize_voice(text, voice_id):
    import uuid, requests
    filename = f"output_{uuid.uuid4().hex}.mp3"
    url = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}"
    headers = {"xi-api-key": ELEVENLABS_API_KEY, "Content-Type": "application/json"}
    data = {"text": text, "voice_settings": {"stability": 0.6, "similarity_boost": 0.9}}

    response = requests.post(url, json=data, headers=headers)

    if response.headers.get("Content-Type") != "audio/mpeg":
        raise ValueError(f"ElevenLabs error: {response.text}")  # 🚨 catch issue

    with open(filename, "wb") as f:
        f.write(response.content)
    return filename

