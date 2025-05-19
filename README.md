# HoloAssistantAi

## Project Status

**IMPORTANT:** HoloAssistantAi is currently under active development and is not intended for production use. This project is being developed for educational and research purposes only. Features and implementation details are subject to change.

## Overview

HoloAssistantAi is a gesture-controlled intelligent assistant that integrates OpenAI's capabilities with audio processing, weather information retrieval, and hand gesture recognition using computer vision.

## Features

- **Gesture Control**: Activate and deactivate the assistant using specific hand gestures
- **Speech Recognition**: Process voice commands and questions
- **Text-to-Speech**: Receive voice responses using OpenAI's TTS model
- **Weather Information**: Get current weather data based on configured location
- **AI Integration**: Utilizes OpenAI's GPT-4o model for generating contextual responses

## Architecture

The project consists of several modules:

- **globals.py**: Configuration and constants
- **audio.py**: Speech synthesis and recognition
- **assistantAi.py**: AI interaction and response management
- **handGesture.py**: Computer vision-based gesture recognition
- **concate.py**: Integration of gesture recognition with assistant functionality
- **main.py**: Application entry point

## Security

The project requires API keys that should be stored securely:
- OpenAI API key
- OpenWeatherMap API key
- Geographic coordinates for weather queries

## Installation

### Prerequisites
- Python 3.8+
- Webcam
- Microphone
- API keys for OpenAI and OpenWeatherMap

### Standard Setup
1. Clone the repository
2. Create a `.env` file in the project root with your API keys (see Environment Variables)
3. Install dependencies: `pip install -r requirements.txt`
4. Run the application: `python ProgramToHologram/main.py`

### Docker Setup
1. Clone the repository
2. Create a `.env` file with your API keys
3. Build the Docker image: `docker build -t holoassistant .`
4. Run the container: `docker run --env-file .env -p 8000:8000 --device=/dev/video0:/dev/video0 holoassistant`

## Environment Variables

Create a `.env` file in the project root with the following variables:
```
OPENAI_API_KEY=your_openai_api_key
WEATHER_API_KEY=your_openweathermap_api_key
LATITUDE=xx.xxxx
LONGITUDE=yy.yyyy
```

## Usage

1. Start the application
2. The webcam interface will open automatically
3. Use the following gestures to control the assistant:
   - **Activate**: Extend thumb and pinky finger while keeping other fingers closed
   - **Deactivate**: Make a fist
4. Speak clearly to interact with the assistant
5. Say "koniec" (end) to terminate the conversation

## Contributing

Contributions are welcome. Please create a pull request with your proposed changes.

## License

<<<<<<< HEAD
This project is licensed under the MIT License - see the LICENSE file for details.

## Disclaimer

This project is for educational purposes only. The developers are not responsible for any misuse or for any damages that may result from using this software.
=======
This project is open source and free to use under the MIT License. Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:

- Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.
- Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
>>>>>>> 2c91a1a (Create README.md)
