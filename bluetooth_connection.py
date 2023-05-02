import sys
from bluetooth import *
from threading import Thread

class BluetoothConnection(Thread):
    def __init__(self):
        Thread.__init__(self)

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
                    if len(data) == 0:
                        break
                    yield data

                except BluetoothError as e:
                    print(f"Error occurred: {e}")
                    print("disconnecting..")
                    client_sock.close()
                    server_socket.close()
                    break
