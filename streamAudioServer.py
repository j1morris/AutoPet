import socket
import pyaudio

# Socket
HOST = '192.168.20.10'
PORT = 5000

# Audio
p = pyaudio.PyAudio()
CHUNK = 1024 * 4
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                output=True,
                frames_per_buffer=CHUNK,
                output_device_index=2)

with socket.socket() as server_socket:
    server_socket.bind((HOST, PORT))
    server_socket.listen(1)
    conn, address = server_socket.accept()
    print("Connection from " + address[0] + ":" + str(address[1]))

    data = conn.recv(4096)
    while data != "":
        data = conn.recv(4096)
        print(data)
        stream.write(data)

stream.stop_stream()
stream.close()
p.terminate()