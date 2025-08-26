from ai_services import generate_response, synthesize_voice
from config import PERSONAS

persona = PERSONAS["elon_musk"]

text = generate_response("What is your vision for Mars?", persona["style"])
print("AI Response:", text)

audio = synthesize_voice(text)
print("Audio file saved:", audio)
