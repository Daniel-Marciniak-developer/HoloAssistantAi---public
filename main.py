from concate import GestureControlledAssistant
import threading


if __name__ == "__main__":
    controller = GestureControlledAssistant()
    gesture_thread = threading.Thread(target=controller.run_gesture_recognition)
    gesture_thread.start()
    gesture_thread.join()