from pathlib import Path
from openai import OpenAI
import speech_recognition
import sounddevice
import soundfile

from globals import Globals


class Speaker:
    def __init__(self) -> None:
        self.client = OpenAI(api_key=Globals.openai_api_key)
        self.speech_file_path = Path(__file__).parent / "speech.mp3"
        
    def speak(self, text:str) -> None:
        response = self._generate_response(text)
        self._save_mp3_file(response)
        self._play_mp3_file()

    def _play_mp3_file(self):
        audio_data, sample_rate = soundfile.read(self.speech_file_path)
        sounddevice.play(audio_data, sample_rate)
        sounddevice.wait()

    def _save_mp3_file(self, response):
        with open(self.speech_file_path, "wb") as f:
            f.write(response.content)

    def _generate_response(self, text):
        response = self.client.audio.speech.create(
            model="tts-1",
            voice="nova",
            input=text
        )
        return response


class Listener:
    def __init__(self) -> None:
        self.listening_active = True 

    def listen(self) -> str:
        recognizer = speech_recognition.Recognizer()
        while self.listening_active:
            with speech_recognition.Microphone() as source:
                print("Lucy nasłuchuje...")
                audio_data = recognizer.listen(source)
                try:
                    text = recognizer.recognize_google(audio_data, language='pl-PL') #recognize_google to jedna z opcji ale jest wiele innych np. recognize_sphinx
                    print("Lucy rozpoznała: " + text)
                    return text
                except speech_recognition.UnknownValueError:
                    pass
                except speech_recognition.RequestError as e:
                    print(f"Lucy napotkała błąd usługi Google Speech Recognition: {e}")
                    
    def stop_listening(self):
        self.listening_active = False
        # print("Nasłuchiwanie zostało wyłączone.")

















