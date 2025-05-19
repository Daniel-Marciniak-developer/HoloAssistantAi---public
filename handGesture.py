from cvzone.HandTrackingModule import HandDetector
from sklearn.manifold import MDS
import numpy as np
import cv2

from globals import Globals


class HandGestureRecognition:
    def __init__(self, controller):
        self.controller = controller
        self.width, self.height = 1280, 720
        self.cap = cv2.VideoCapture(0)
        self.globals = Globals()
        self.cap.set(3, self.width)
        self.cap.set(4, self.height)
        self.detector = HandDetector(detectionCon=0.8, maxHands=1)
        self.mesure_time_for_calling, self.mesure_time_for_fist = self.globals.mesure_time_for_calling, self.globals.mesure_time_for_fist

    def hand_points(self, hand):
        fingers = hand['lmList']
        transformed_fingers = self.transform_landmarks(fingers)

        palm_base = transformed_fingers[0]
        thumb_tip = transformed_fingers[4]
        index_finger_MCP = transformed_fingers[5]
        index_tip = transformed_fingers[8]
        middle_finger_tip = transformed_fingers[12]
        ring_finger_tip = transformed_fingers[16]
        pinky_tip = transformed_fingers[20]
        return palm_base,thumb_tip,index_finger_MCP,index_tip,middle_finger_tip,ring_finger_tip,pinky_tip

    def transform_landmarks(self, landmarks):
        mds = MDS(normalized_stress='auto')
        landmarks = np.array(landmarks)
        transformed = mds.fit_transform(landmarks[:, :2])
        return transformed

    def scale_distance(self, ref_length, distance):
        return distance / ref_length if ref_length != 0 else 0
    
    def calculate_distance(self, p1, p2):
        return np.linalg.norm(np.array(p1) - np.array(p2))

    def calculate_angle(self, p1, p2, p3):
        a = np.linalg.norm(np.array(p2) - np.array(p3))
        b = np.linalg.norm(np.array(p1) - np.array(p3))
        c = np.linalg.norm(np.array(p1) - np.array(p2))
        angle = np.arccos((a**2 + c**2 - b**2) / (2 * a * c))
        return np.degrees(angle)
    
    def distance_between(self, palm_base, thumb_tip, index_tip, middle_finger_tip, ring_finger_tip, pinky_tip, reference_length):
        thumb_dist = self.scale_distance(reference_length, self.calculate_distance(palm_base, thumb_tip))
        index_tip_dist = self.scale_distance(reference_length, self.calculate_distance(palm_base, index_tip))
        middle_tip_dist = self.scale_distance(reference_length, self.calculate_distance(palm_base, middle_finger_tip))
        ring_tip_dist = self.scale_distance(reference_length, self.calculate_distance(palm_base, ring_finger_tip))
        pinky_dist = self.scale_distance(reference_length, self.calculate_distance(palm_base, pinky_tip))
        thumb_and_pinky_angle = self.calculate_angle(thumb_tip, palm_base, pinky_tip)
        return thumb_dist,index_tip_dist,middle_tip_dist,ring_tip_dist,pinky_dist,thumb_and_pinky_angle

    def classify_gesture(self, hand) -> str:
        palm_base, thumb_tip, index_finger_MCP, index_tip, middle_finger_tip, ring_finger_tip, pinky_tip = self.hand_points(hand)
        reference_length = self.calculate_distance(palm_base, index_finger_MCP)
        thumb_dist, index_tip_dist, middle_tip_dist, ring_tip_dist, pinky_dist, thumb_and_pinky_angle = self.distance_between(palm_base, thumb_tip, index_tip, middle_finger_tip, ring_finger_tip, pinky_tip, reference_length)

        if thumb_dist > 1.15 and pinky_dist > 1.30 and thumb_and_pinky_angle > 60 and index_tip_dist < 1.1 and middle_tip_dist < self.globals.threshold and ring_tip_dist < self.globals.threshold:
            self.mesure_time_for_calling += 1
            self.detected_gesture()
            return "Calling Lucy"
        if abs(thumb_dist) < 1.15 and abs(index_tip_dist) < 1.1 and abs(middle_tip_dist) < self.globals.threshold and abs(ring_tip_dist) < self.globals.threshold and abs(pinky_dist) < self.globals.threshold:
            self.mesure_time_for_fist += 1
            self.detected_gesture()
            return "Fist"
        return "Hand"
    
    def detected_gesture(self):
        if self.mesure_time_for_calling == 13:
            self.mesure_time_for_calling = 0
            return self.mesure_time_for_calling
        if self.mesure_time_for_fist == 13:
            self.mesure_time_for_fist = 0
            return self.mesure_time_for_fist
        return self.mesure_time_for_fist, self.mesure_time_for_calling
    
    def close(self):
        self.cap.release()
        cv2.destroyAllWindows()

    def run(self):
        success, img = self.cap.read()
        if not success:
            return None
        img = cv2.flip(img, 1)
        hands, img = self.detector.findHands(img, flipType=False)
        gesture = "Hand"
        if hands:
            hand = hands[0]
            gesture = self.classify_gesture(hand)
            print(f"Detected gesture: {gesture}")
        cv2.imshow("Image", img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            self.close()
            return None
        return gesture
