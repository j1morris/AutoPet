import os
import time

from detectPet import *

def debug(msg):
    print("[MAIN] " + str(msg))


def main():

    debug("ENTERING MAIN")
    camera = CameraSensorDriver( source="http://192.168.20.11:8080/stream/video.mjpeg"
                               , crop=( (300,100)
                                      , (600,1000)
                                      )
                               , threshold=0.97
                               )

    # speaker = SpeakerDriver( destination="C0:28:8D:7F:37:C1"
    #                        , sound="/home/pi/Downloads/file_example_WAV_1MG.wav"
    #                        )

    debug("BEFORE WHILE")
    while True:

        # Check if a pet is detected
        detected = camera.detect()
        debug(detected)

        # if detected:

        #     # Scream at the pet
        #     speaker.play()

        time.sleep(1)


if __name__ == "__main__":
    main()
