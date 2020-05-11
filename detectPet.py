from cosineSimilarity import calculate as cosine
import cv2

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

        # Capture initial frame for referrence
        ret, frame = self.device.read()
        resized = cv2.resize(frame, (1280,720))
        self.reference = resized[self.top:self.bottom, self.left:self.right]

    def detect(self):

        # Capture the current frame
        ret, frame = self.device.read()
        resized = cv2.resize(frame, (1280,720))
        current = resized[self.top:self.bottom, self.left:self.right]

        # Calculate cosine similarity
        similarity = cosine(self.reference, current)
        detected = similarity < self.threshold

        print("[CAMERA] similarity = {}, threshold = {}, result = {}".format(similarity, self.threshold, detected))

        # Update reference if needed
        if not detected:
            self.reference = current
        
        return detected

    def __del__(self):
        self.device.release()
        

    


