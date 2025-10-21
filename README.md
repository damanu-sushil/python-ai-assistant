# 🤖 AIDEN - Advanced AI Assistant

<div align="center">

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?logo=javascript&logoColor=black)
![WebSocket](https://img.shields.io/badge/WebSocket-010101?logo=socketdotio&logoColor=white)
![AI](https://img.shields.io/badge/AI-Powered-00d4ff)
![License](https://img.shields.io/badge/License-MIT-green.svg)

**A modern, real-time AI assistant with voice and text capabilities**

[Features](#features) • [Installation](#installation) • [Usage](#usage) • [Tech Stack](#tech-stack) • [Contributing](#contributing)

</div>

---

## ✨ Features

- 💬 **Natural Conversation** - Intuitive chat interface with AI-powered responses
- 🎤 **Voice Input** - Speak naturally to interact with the assistant
- 🔊 **Text-to-Speech** - Hear responses with built-in speech synthesis
- ⚡ **Real-time Communication** - WebSocket-based instant messaging
- 🎨 **Modern UI** - Beautiful, animated interface with glassmorphism design
- 📱 **Responsive Design** - Works seamlessly on desktop and mobile devices
- 📚 **Chat History** - Review and reuse previous conversations
- 🌐 **Cross-Browser** - Compatible with Chrome, Firefox, Edge, and Safari

---

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- Modern web browser (Chrome, Firefox, Edge, or Safari)
- Internet connection for AI API

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/damanu-sushil/python-ai-assistant.git
   cd python-ai-assistant
   ```

2. **Run the application**
   
   **On Windows:**
   ```bash
   .\run_app.bat
   ```
   
   **On Linux/Mac:**
   ```bash
   chmod +x run_app.sh
   ./run_app.sh
   ```

3. **Access the application**
   
   Open your browser and navigate to:
   ```
   http://localhost:5000
   ```

The `run_app.bat` script will automatically:
- Create necessary folders
- Install required dependencies
- Start the Flask server
- Launch the application

---

## 📖 Usage

### Text Mode
1. Type your message in the input field
2. Press `Enter` or click the send button
3. Wait for AI response

### Voice Mode
1. Click the "Voice" button to switch modes
2. Click the microphone button to start speaking
3. Speak your question or command
4. The assistant will respond with both text and voice

### Additional Controls
- 🗑️ **Clear** - Reset the conversation
- ⏹️ **Stop** - Stop text-to-speech playback
- 📚 **History** - View and reuse previous messages

---

## 🛠️ Tech Stack

### Frontend
- **HTML5** - Semantic markup and structure
- **CSS3** - Modern styling with animations and gradients
- **JavaScript (ES6+)** - Interactive functionality and WebSocket client
- **Web Speech API** - Voice recognition and synthesis

### Backend
- **Python 3.8+** - Core backend logic
- **Flask** - Web framework and server
- **WebSocket** - Real-time bidirectional communication
- **AI/ML Libraries** - Natural language processing

### Features
- Glassmorphism UI design
- Animated background with floating orbs
- Real-time typing indicators
- Responsive grid layouts
- Smooth transitions and hover effects

---

## 📁 Project Structure

```
python-ai-assistant/
├── app.py                 # Main Flask application
├── run_app.bat           # Windows startup script
├── run_app.sh            # Linux/Mac startup script
├── requirements.txt      # Python dependencies
├── static/
│   └── aiden-pro.html   # Frontend UI
├── templates/           # Additional HTML templates
├── models/              # AI model files
└── README.md           # This file
```

---

## ⚙️ Configuration

### Environment Variables

Create a `.env` file in the root directory:

```env
FLASK_APP=app.py
FLASK_ENV=development
PORT=5000
AI_API_KEY=your_api_key_here
```

### Customization

Edit `aiden-pro.html` to customize:
- Color scheme (CSS variables in `:root`)
- UI components and layout
- Welcome messages and capabilities
- Animation speeds and effects

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 🐛 Troubleshooting

### Voice input not working
- Ensure you're using a supported browser (Chrome, Edge, Safari)
- Check microphone permissions in browser settings
- Try accessing via HTTPS (required for some browsers)

### WebSocket connection fails
- Check if port 5000 is available
- Verify firewall settings
- Ensure the Flask server is running

### AI not responding
- Check your internet connection
- Verify AI API key configuration
- Review console logs for errors

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- Built with modern web technologies
- Inspired by conversational AI interfaces
- Thanks to all contributors and users

---

## 📞 Support

For issues, questions, or suggestions:
- 🐛 [Report a bug](https://github.com/damanu-sushil/python-ai-assistant/issues)
- 💡 [Request a feature](https://github.com/damanu-sushil/python-ai-assistant/issues)
- 📧 Contact: [your-email@example.com]

---

<div align="center">

**Made with ❤️ by the AIDEN Team**

⭐ Star this repo if you find it helpful!

</div>
