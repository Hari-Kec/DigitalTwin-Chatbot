# 🤖 AI Persona Chatbot

A persona-based AI chatbot built with Streamlit, OpenAI, and ElevenLabs. Currently features Elon Musk as the primary persona, with the ability to extend to more personalities.

## 🚀 Features

- **Persona-Based AI**: Chat with AI that emulates specific personalities (currently Elon Musk)
- **Voice Generation**: ElevenLabs integration for realistic voice synthesis
- **Interactive UI**: Clean Streamlit interface with avatar-based navigation
- **Conversation History**: Maintains chat history during sessions
- **Extensible Architecture**: Easy to add new personas

## 🛠️ Tech Stack

- **Frontend**: Streamlit
- **AI Language Model**: OpenAI GPT-3.5-turbo
- **Voice Synthesis**: ElevenLabs API
- **Configuration**: Python-dotenv
- **Image Processing**: Pillow

## 📁 Project Structure

```
Digital Clone/
├── app.py                 # Main Streamlit application
├── config.py             # Configuration and persona definitions
├── ai_services.py        # OpenAI and ElevenLabs API handlers
├── chat_session.py       # Chat session management
├── ui_components.py      # Streamlit UI components
├── requirements.txt      # Python dependencies
├── env_example.txt       # Environment variables template
└── README.md            # This file
```

## 🚀 Quick Start

### 1. Clone and Setup

```bash
# Navigate to your project directory
cd "Digital Clone"

# Install dependencies
pip install -r requirements.txt
```

### 2. Configure API Keys

1. Copy the environment template:

   ```bash
   cp env_example.txt .env
   ```

2. Edit `.env` and add your API keys:
   ```env
   OPENAI_API_KEY=your_openai_api_key_here
   ELEVENLABS_API_KEY=your_elevenlabs_api_key_here
   ELEVENLABS_VOICE_ID=your_voice_id_here
   ```

### 3. Get API Keys

#### OpenAI API Key

1. Visit [OpenAI Platform](https://platform.openai.com/)
2. Sign up or log in
3. Navigate to API Keys section
4. Create a new API key
5. Copy and paste into your `.env` file

#### ElevenLabs API Key

1. Visit [ElevenLabs](https://elevenlabs.io/)
2. Sign up for a free account
3. Go to your profile settings
4. Copy your API key
5. Paste into your `.env` file

### 4. Run the Application

```bash
streamlit run app.py
```

The application will open in your browser at `http://localhost:8501`

## 🎯 Usage

### Dashboard

- The main page shows available personas (currently Elon Musk)
- Click on the avatar to start a chat session

### Chat Interface

- **Text Input**: Type your message in the text area
- **Send**: Send text-only response
- **Generate Voice**: Send message and get voice response
- **Clear Chat**: Reset conversation history
- **Back to Dashboard**: Return to persona selection

### Voice Features

- Click "Generate Voice" to hear AI responses
- Audio files are automatically generated and played
- Temporary files are cleaned up automatically

## 🎭 Current Personas

### Elon Musk

- **Personality**: Visionary CEO of Tesla, SpaceX, and X
- **Speaking Style**: Direct, technical, sometimes controversial
- **Topics**: Innovation, Mars, AI, sustainable energy, technology
- **Voice**: ElevenLabs voice synthesis

## 🔧 Adding New Personas

To add a new persona, edit `config.py` and add to the `PERSONAS` dictionary:

```python
PERSONAS = {
    'elon_musk': {
        'name': 'Elon Musk',
        'avatar_url': 'https://example.com/avatar.jpg',
        'system_prompt': 'You are Elon Musk...'
    },
    'new_persona': {
        'name': 'New Persona Name',
        'avatar_url': 'https://example.com/new_avatar.jpg',
        'system_prompt': 'You are [persona description]...'
    }
}
```

## 🎨 Customization

### Styling

- Modify CSS in `app.py` for custom styling
- Update avatar images and URLs in `config.py`
- Adjust voice settings in ElevenLabs configuration

### AI Behavior

- Edit system prompts in `config.py` to change persona behavior
- Adjust OpenAI parameters in `ai_services.py`
- Modify conversation history handling in `chat_session.py`

## 🔍 Troubleshooting

### Common Issues

1. **API Key Errors**

   - Ensure all API keys are correctly set in `.env`
   - Check that the `.env` file is in the project root
   - Verify API keys are valid and have sufficient credits

2. **Voice Generation Issues**

   - Check ElevenLabs API key and voice ID
   - Ensure you have sufficient ElevenLabs credits
   - Verify internet connection for API calls

3. **Avatar Loading Issues**

   - Check avatar URLs in `config.py`
   - Ensure images are publicly accessible
   - Verify internet connection

4. **Streamlit Issues**
   - Update Streamlit: `pip install --upgrade streamlit`
   - Clear browser cache
   - Restart the application

### Error Messages

- **"Missing required API keys"**: Add missing API keys to `.env`
- **"Error loading avatar"**: Check avatar URL and internet connection
- **"Error generating voice"**: Verify ElevenLabs configuration

## 📝 Development

### Project Structure

- `app.py`: Main application entry point
- `config.py`: Configuration and persona definitions
- `ai_services.py`: API service handlers
- `chat_session.py`: Session and conversation management
- `ui_components.py`: Streamlit UI components

### Adding Features

1. **New Personas**: Add to `config.py` PERSONAS dictionary
2. **UI Enhancements**: Modify `ui_components.py`
3. **AI Improvements**: Update `ai_services.py`
4. **Session Features**: Extend `chat_session.py`

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📄 License

This project is open source and available under the MIT License.

## 🙏 Acknowledgments

- OpenAI for GPT-3.5-turbo
- ElevenLabs for voice synthesis
- Streamlit for the web framework
- The open-source community for inspiration

---

**Note**: This is a demo application. Please ensure you comply with OpenAI and ElevenLabs terms of service and usage policies.
