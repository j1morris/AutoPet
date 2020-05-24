import socket
import pyaudio

# Socket
HOST = '192.168.20.10'
print(HOST)
exit()
PORT = 5000

# Audio
CHUNK = 1024 * 4
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
p = pyaudio.PyAudio()
stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)

print("Recording")

with socket.socket() as client_socket:
    client_socket.connect((HOST, PORT))
    while True:
        data = stream.read(CHUNK)
        client_socket.send(data)