from openai import OpenAI
import requests

from audio import Speaker, Listener
from globals import Globals

class StaticInfo:
    def __init__(self, assistant=None) -> None:
        self.weather_api_key = Globals.weather_api_key
        self.lat, self.lon = Globals.latitude, Globals.longitude
        self.base_url = Globals.base_url
        self.assistant = assistant
        
    def _weather_info(self):
        complete_url = f"{self.base_url}?lat={self.lat}&lon={self.lon}&appid={self.weather_api_key}&units=metric"
        response = requests.get(complete_url)
        return response.json()
    
    def time_info():
        "To do"
        pass
    
    def weather_response(self) -> str:
        weather_data = self._weather_info()
        if weather_data.get("cod") != 200:
            response = "Nie udało się uzyskać danych o pogodzie."
        else:
            temperature = round(weather_data["main"]["temp"])
            weather_description = weather_data["weather"][0]["description"]
            response = self.assistant.provide_assistance(
                f"Aktualna temperatura w Kaliszu to {temperature} stopni Celsjusza. Pogoda jest {weather_description}."
            )
        return response

    def time_resposne(self):
        "To do"
        pass
    

class Assistant:
    def __init__(self, static_info=None) -> None:
        self.client = OpenAI(api_key=Globals.openai_api_key)
        self.static_info = static_info or StaticInfo(assistant=self)
        self.listener = Listener()
        self.speaker = Speaker()
        self.active = False

    def assistant_activated(self):
        if not self.active:
            self.active = True
            print("Asystent został aktywowany...")

    def assistant_deactivated(self):
        if self.active:
            self.active = False
            self.listener.stop_listening() 
            self.speaker.speak("Do zobaczenia!")
            print("Asystent dezaktywowany.")

    def _generate_response_AI(self, text, system_message):
        response = self.client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": system_message},
                {"role": "user", "content": text}
            ]
        )
        return response
    
    def provide_assistance(self, text, is_assistance_requested=False) -> str:
        system_message = Globals.rewrite_message_Ai
        if is_assistance_requested:
            system_message += Globals.structure_massage_Ai

        response = self._generate_response_AI(text, system_message)
        
        if response.choices:
            return response.choices[0].message.content.strip()

        return "Błąd odpowiedzi"

    def concate_Assistant_and_Audio(self):
        self.listener.listening_active = True
        while self.active:
            if not self.active:
                break

            question = self.listener.listen()
            if question:
                question = question.lower()
                print(f"Otrzymane pytanie: {question}")

            if "koniec" in question:
                self.assistant_deactivated()
                break

            if "pogoda" in question:
                response = self.static_info.weather_response()
            else:
                response = self.provide_assistance(question, is_assistance_requested=True)

            self.speaker.speak(response)
            print(f"Odpowiedź Lucy: {response}")
