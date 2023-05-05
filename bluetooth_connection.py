import sys
from bluetooth import *
from threading import Thread, Timer
import api_requests
import time

def contains_digits(s):
    return any(c.isdigit() for c in s)

class BluetoothConnection(Thread):
    def __init__(self, data_queue):
        Thread.__init__(self)
        self.data_queue = data_queue
        self.client_sock = None
        self.heartbeat_thread = None

    def send_heartbeat(self):
        while self.client_sock:
            try:
                self.client_sock.send(b'1')
                print("beat")
            except BluetoothError as e:
                print(f"Error occurred while sending heartbeat: {e}")
            time.sleep(5)  # Wait for 5 seconds before sending the next heartbeat


    def run(self):
        while True:
            server_socket = BluetoothSocket(RFCOMM)
            server_socket.bind(("", PORT_ANY))
            server_socket.listen(1)
            print("waiting for client to connect...")
            port = server_socket.getsockname()[1]

            uuid = "30097c35-95b9-4f92-9d2e-e3e06aa3b07f"

            advertise_service(server_socket, "PleaseWork", service_id=uuid, service_classes=[uuid, SERIAL_PORT_CLASS], profiles=[SERIAL_PORT_PROFILE])

            self.client_sock, client_info = server_socket.accept()
            print(client_info)

            self.heartbeat_thread = Thread(target=self.send_heartbeat)  # Create a thread for sending heartbeats
            self.heartbeat_thread.start()  # Start the heartbeat thread

            while True:
                try:
                    data = self.client_sock.recv(1024).decode('utf-8')
                    if not contains_digits(data):
                        data = data.strip()

                    if len(data) == 0:
                        break
                    # Handle received data
                    if data == "START_SESSION":
                        print("Attempting to start session...")

                        def handle_start_session():
                            status_code = api_requests.start_mow_session()
                            print(status_code)
                            if status_code == 201:
                                self.data_queue.put(data)  # Add received data to the queue
                                self.client_sock.send("Success".encode('utf-8'))
                            else:
                                self.client_sock.send("Failure".encode('utf-8'))

                        start_session_thread = Thread(target=handle_start_session)
                        start_session_thread.start()

                    elif data == "END_SESSION":
                        print("Attempting to end session...")

                        def handle_end_session():
                            status_code = api_requests.end_mow_session()
                            if status_code == 200:
                                self.client_sock.send("Success".encode('utf-8'))
                                self.data_queue.put(data)  # Add received data to the queue
                            else:
                                self.client_sock.send("Failure".encode('utf-8'))

                        end_session_thread = Thread(target=handle_end_session)
                        end_session_thread.start()

                    else:
                        self.data_queue.put(data)  # Add received data to the queue

                except BluetoothError as e:
                    print(f"Error occurred: {e}")
                    print("disconnecting..")
                    self.client_sock.close()
                    server_socket.close()
                    break
