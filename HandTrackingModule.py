"""
Hand Tracing Module
By: Murtaza Hassan
Youtube: http://www.youtube.com/c/MurtazasWorkshopRoboticsandAI
Website: https://www.computervision.zone
"""

from operator import length_hint
import cv2
import mediapipe as mp
import time


class handDetector():
    def __init__(self, mode=False, maxHands=2, detectionCon=0.5, trackCon=0.5):
        self.mode = mode
        self.maxHands = maxHands
        self.detectionCon = detectionCon
        self.trackCon = trackCon

        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands() #self.mode, self.maxHands,self.detectionCon, self.trackCon)
        self.mpDraw = mp.solutions.drawing_utils
        self.no_of_hands = 0

    def find_no_of_hands(self, img):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(imgRGB)
        return self.results.multi_hand_landmarks.count()

    def findHands(self, img, draw=True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(imgRGB)
        # print(results.multi_hand_landmarks)
        h,w,c = img.shape

        self.detected_hands = set()
        count =0
        if self.results.multi_hand_landmarks:
            for handLms in self.results.multi_hand_landmarks:
                count +=1 
                self.detected_hands.add(count)
                if draw:
                    self.mpDraw.draw_landmarks(img, handLms, self.mpHands.HAND_CONNECTIONS)
        
        self.no_of_hands = len(self.detected_hands)
        return img

    def findPosition(self, img, handNo=0, draw=True):
        lmList = []

        try:
            if self.results.multi_hand_landmarks:
                myHand = self.results.multi_hand_landmarks[handNo]
                if myHand:
                    for id, lm in enumerate(myHand.landmark):
                        #print(id, lm)
                        h, w, c = img.shape
                        cx, cy, cz = int(lm.x * w), int(lm.y * h), int(lm.z * c * w)
                        #print(id, cx, cy,cz)
                        lmList.append([id, cx, cy,cz])

                        if draw:
                            cv2.circle(img, (cx, cy), 15, (255, 0, 255), cv2.FILLED)
        except IndexError:
            #print("IndexError")
            return lmList 
        except:
            return lmList 
        return lmList


def main():
    pTime = 0
    cTime = 0
    cap = cv2.VideoCapture(0)
    detector = handDetector()
    while True:
        success, img = cap.read()
        if img is None:
            break
        img = detector.findHands(img)
        left_lmList = detector.findPosition(img,0)
        if len(left_lmList) != 0:
            print(left_lmList)

        right_lmList = detector.findPosition(img,1)
        if len(right_lmList) != 0:
            print(right_lmList)

        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime

        cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3,
                    (255, 0, 255), 3)

        cv2.imshow("Image", img)
        cv2.waitKey(1)


if __name__ == "__main__":
    main()

