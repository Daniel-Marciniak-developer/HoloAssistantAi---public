import threading
import time

from handGesture import HandGestureRecognition
from assistantAi import Assistant
from globals import Globals

class GestureControlledAssistant:
    def __init__(self):
        self.assistant = Assistant()
        self.gesture_recognition = HandGestureRecognition(self)
        self.stop_event = threading.Event()
        self.globals = Globals()
        self.assistant_thread = None

    def gesture_action(self, gesture):
        if gesture == "Calling Lucy" and self.gesture_recognition.mesure_time_for_calling == 12:
            #print("Aktywowanie asystenta...")
            if not self.assistant.active:
                self.assistant.assistant_activated()
                self.stop_event.clear()
                self.assistant_thread = threading.Thread(target=self.assistant_main_wrapper)
                self.assistant_thread.start()
        elif gesture == "Fist" and self.gesture_recognition.mesure_time_for_fist == 12:
            #print("Dezaktywowanie asystenta...")
            if self.assistant.active:
                self.assistant.assistant_deactivated()
                self.stop_event.set()
                if self.assistant_thread and self.assistant_thread.is_alive():
                    self.assistant_thread.join()
                self.assistant_thread = None
        elif gesture == "Hand":
            pass
    
    def assistant_main_wrapper(self):
        while not self.stop_event.is_set() and self.assistant.active:
            self.assistant.concate_Assistant_and_Audio()
            time.sleep(0.1)

    def run_gesture_recognition(self):
        while True:
            gesture = self.gesture_recognition.run()
            self.gesture_action(gesture)
            time.sleep(0.1)