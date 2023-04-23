import sys
sys.path.append('/home/admin/.local/lib/python3.9/site-packages')
import time
import serial
import threading
from bluetooth import *
from picamera2 import Picamera2
import api_requests

API_KEY = 'your_api_key'  # Replace with your API key

# Initialize camera
picam2 = Picamera2()

# Set up serial connection
ser = serial.Serial('/dev/ttyUSB0', 9600)

# Bluetooth connection
def bluetooth_connection():
    while True:
        server_socket = BluetoothSocket(RFCOMM)
        server_socket.bind(("", PORT_ANY))
        server_socket.listen(1)
        print("waiting for client to connect...")

        port = server_socket.getsockname()[1]

        uuid = "30097c35-95b9-4f92-9d2e-e3e06aa3b07f"

        advertise_service(server_socket,
                          "PleaseWork",
                          service_id=uuid,
                          service_classes=[uuid, SERIAL_PORT_CLASS],
                          profiles=[SERIAL_PORT_PROFILE]
                          )

        print("asdfasdf")
        client_sock, client_info = server_socket.accept()
        print(client_info)

        while True:
            try:
                data = client_sock.recv(1024).decode('utf-8')
                if len(data) == 0: break
                ser.write(data.encode())
            except BluetoothError as e:
                print(f"Error occurred: {e}")
                print("disconnecting..")
                client_sock.close()
                server_socket.close()
                break
       
# Start Bluetooth connection thread
bt_thread = threading.Thread(target=bluetooth_connection)
bt_thread.daemon = True
bt_thread.start()

# Main loop
while True:
    # Read signals from arduino
    signal = ser.readline().decode().strip()
    print(signal)
    if signal == "TAKE_PICTURE":
        try:
            picam2.start_and_capture_file("test.jpg", delay=3, show_preview=False)
            print('Picture taken successfully!')
        except Exception as e:
            print('Error taking picture:', e)
    elif signal == "START_MOW_SESSION":
        api_requests.start_mow_session(API_KEY)
    elif signal.startswith("UPDATE_POSITION"):
        _, xPos, yPos = signal.split(',')
        api_requests.update_mower_position(API_KEY, xPos, yPos)
    elif signal == "END_MOW_SESSION":
        api_requests.end_mow_session(API_KEY)
    else:
        print("Unknown signal")
