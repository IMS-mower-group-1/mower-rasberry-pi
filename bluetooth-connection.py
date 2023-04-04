import bluetooth

# Define the Bluetooth socket parameters
server_socket = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
port = 1 # RFCOMM port number
server_socket.bind(("", bluetooth.PORT_ANY))
server_socket.listen(1) # Maximum number of queued connections

# Wait for a Bluetooth client to connect
print("Waiting for a Bluetooth client...")
client_socket, client_adress = server_socket.accept()
print(f"Accepted connection from {client_adress}")

# Send data to the client
#data = "Hello, client!"
#client_socket.send(data)

# Close the sockets
#client_socket.close()
#server_socket.close()
