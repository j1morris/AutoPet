import os
import time

from drivers import *

TM_BETWEEN_SOUNDS = 60
MAX_ATTEMPTS = 5

def debug(msg):
    print("[ MAIN ] " + str(msg))


def main():

    prev_detected = False
    prev_time = 0
    num_attempts = 0

    debug("ENTERING MAIN")
    camera = CameraSensorDriver( source="http://192.168.20.11:8080/stream/video.mjpeg"
                               , crop=( (300,100)
                                      , (600,1000)
                                      )
                               , threshold=0.97
                               )

    speaker = SpeakerDriver( destination="C0:28:8D:7F:37:C1" )

    debug("BEFORE WHILE")
    while True:

        # Check if a pet is detected
        detected = camera.detect()
        debug(detected)

        if detected:

            curr_time = time.time()
            if curr_time - prev_time > TM_BETWEEN_SOUNDS:

                # Only try the voice command a set number of times
                if num_attempts < MAX_ATTEMPTS:

                  # Scream at the pet
                  debug("GetOff.wav")
                  speaker.play("/home/pi/Downloads/GetOff.wav")
                  prev_time = curr_time

                  num_attempts = num_attempts + 1

        else:
            prev_time = 0
            num_attempts = 0

        if prev_detected and not detected:

            debug("GoodBoy.wav")
            speaker.play("/home/pi/Downloads/GoodBoy.wav")

        prev_detected = detected

        time.sleep(2)
        # input("Press <enter> to continue")


if __name__ == "__main__":
    main()
