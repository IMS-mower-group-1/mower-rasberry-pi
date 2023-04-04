from bluetooth import *

server_socket = BluetoothSocket(RFCOMM)
server_socket.bind(("",PORT_ANY))
server_socket.listen(1)
print("waiting for client to connect...")

port = server_socket.getsockname()[1]

uuid = "30097c35-95b9-4f92-9d2e-e3e06aa3b07f"

advertise_service(server_socket,
"PleaseWork",
service_id=uuid,
service_classes = [uuid, SERIAL_PORT_CLASS],
profiles = [SERIAL_PORT_PROFILE]
)


print("asdfasdf")
client_sock, client_info = server_socket.accept()
print(client_info)


while True:
	print("test")
	data = client_sock.recv(1024)
	if len(data) == 0: break
	print(data)

print("disc")

client_sock.close()
server_socket.close()

