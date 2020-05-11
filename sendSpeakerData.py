#Connect speaker
#echo -e "connect C0:28:8D:7F:37:C1" | bluetoothctl
#Disconnect speaker
#echo -e "disconnect C0:28:8D:7F:37:C1" | bluetoothctl
#play sample
#aplay -D bluealsa:DEV=C0:28:8D:7F:37:C1 <AUDIOFILE.wav>
#Control volume
#amixer -D bluealsa sset "UE BOOM 2 - A2DP" <VOLUME%>
#Speaker status
#alsamixer -D bluealsa
#source https://www.sigmdel.ca/michel/ha/rpi/bluetooth_02_en.html#bluez
#aplay
#https://linux.die.net/man/1/aplay

import os

for i in range(2):
    print("Before aplay")
    os.system("aplay -D bluealsa:DEV=C0:28:8D:7F:37:C1 /home/pi/Downloads/file_example_WAV_1MG.wav")
    print("After aplay")
