import os

env_path = ".env"
if not os.path.exists(env_path):
    open(env_path, "w").write("OPENAI_API_KEY=\nELEVEN_API_KEY=\nELEVEN_VOICE_ID=\n")
    print("✅ .env file created. Fill in your API keys.")
else:
    print("⚡ .env file already exists.")
