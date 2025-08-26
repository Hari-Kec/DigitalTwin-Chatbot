from config import OPENAI_API_KEY, ELEVENLABS_API_KEY, ELEVENLABS_VOICE_ID

print("OpenAI Key:", "Loaded" if OPENAI_API_KEY else "Missing")
print("ElevenLabs Key:", "Loaded" if ELEVENLABS_API_KEY else "Missing")
print("Voice ID:", "Loaded" if ELEVENLABS_VOICE_ID else "Missing")
