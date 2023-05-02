import sys
from bluetooth import *
from threading import Thread
import api_requests

def contains_digits(s):
    return any(c.isdigit() for c in s)

class BluetoothConnection(Thread):
    def __init__(self, data_queue):
        Thread.__init__(self)
        self.data_queue = data_queue
        
    def run(self):
        while True:
            server_socket = BluetoothSocket(RFCOMM)
            server_socket.bind(("", PORT_ANY))
            server_socket.listen(1)
            print("waiting for client to connect...")
            port = server_socket.getsockname()[1]

            uuid = "30097c35-95b9-4f92-9d2e-e3e06aa3b07f"

            advertise_service(server_socket, "PleaseWork", service_id=uuid, service_classes=[uuid, SERIAL_PORT_CLASS], profiles=[SERIAL_PORT_PROFILE])

            client_sock, client_info = server_socket.accept()
            print(client_info)

            while True:
                try:
                    data = client_sock.recv(1024).decode('utf-8')
                    if not contains_digits(data):
                        data = data.strip()

                    if len(data) == 0:
                        break
                    # Handle received data
                    if data == "START_SESSION":
                        print("Attempting to start session...")
                        status_code = api_requests.start_mow_session()
                        if status_code == 201:
                            self.data_queue.put(data)  # Add received data to the queue
                    elif data == "END_SESSION":
                        print("Attempting to end session...")
                        status_code = api_requests.end_mow_session()
                        if status_code == 200:
                            self.data_queue.put(data)  # Add received data to the queue
                    else:
                        self.data_queue.put(data)  # Add received data to the queue

                except BluetoothError as e:
                    print(f"Error occurred: {e}")
                    print("disconnecting..")
                    client_sock.close()
                    server_socket.close()
                    break
