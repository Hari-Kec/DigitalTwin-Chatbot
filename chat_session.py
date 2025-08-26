from ai_services import generate_response, synthesize_voice

class ChatSession:
    def __init__(self, persona):
        self.persona = persona
        self.history = []

    def add_message(self, role, content):
        self.history.append({"role": role, "content": content})

    def get_response(self, user_input):
        self.add_message("user", user_input)
        response = generate_response(user_input, self.persona["style"])
        self.add_message("assistant", response)
        audio_file = synthesize_voice(response, self.persona["voice_id"])
        return response, audio_file
