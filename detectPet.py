from cosineSimilarity import calculate as cosine
import os
import json
import cv2
from datetime import datetime

class SensorDriver:
    def __init__():
        pass
    def detect():
        pass

class CameraSensorDriver(SensorDriver):

    def __init__(self, source, crop=((300,100), (600, 1000)), threshold=0.95):
        
        self.device = cv2.VideoCapture()
        self.device.open(source)
        (self.top, self.left), (self.bottom, self.right) = crop
        self.threshold = threshold
        self.frameid = 1

        # Capture initial frame for referrence
        ret, frame = self.device.read()
        resized = cv2.resize(frame, (1280,720))
        self.reference = resized[self.top:self.bottom, self.left:self.right]
        self.refid = 0

        # Book Keeping object
        self.stats = {
                'similarity': [],
                'refid': [],
                'detected': []
        }

        now = datetime.now()
        self.date_time = now.strftime("%m_%d_%Y_%H_%M_%S")
        os.mkdir("./data/savedFrames_{}".format(self.date_time))
        self.saveFrame(resized)

    def detect(self):


        # Capture the current frame
        ret, frame = self.device.read()
        resized = cv2.resize(frame, (1280,720))
        current = resized[self.top:self.bottom, self.left:self.right]

        # Calculate cosine similarity
        similarity = cosine(self.reference, current)
        detected = similarity < self.threshold

        print("[CAMERA] similarity = {}, threshold = {}, result = {}".format(similarity, self.threshold, detected))

        # Book keeping
        self.stats['similarity'].append(similarity)
        self.stats['refid'].append(self.refid)
        self.stats['detected'].append(1 if detected else 0)
        self.saveFrame(resized)

        # Update reference if needed
        if not detected:
            self.reference = current
            self.refid = self.frameid

        # Update the frameid for the next frame
        self.frameid += 1

        return detected

    def __del__(self):
        self.device.release()
        

    def saveFrame(self, frame):
        cv2.imwrite('./data/savedFrames_{}/frame_{}.jpg'.format(self.date_time, str(self.frameid)), frame)
        self.saveStats()

    def saveStats(self):
        with open('./data/savedFrames_{}/stats.json'.format(self.date_time), 'w') as f:
            json.dump(self.stats, f, indent=4)

        # Save a copy to the server folder
        with open('./web_ui/server/stats.json', 'w') as f:
            json.dump(self.stats, f, indent=4)

class SpeakerDriver:

    def __init__(self, destination):
        
        self.destination = destination

    def play(self, sound):
        self.command = "aplay -D bluealsa:DEV={} {}".format(self.destination, sound)
        os.system(self.command)


