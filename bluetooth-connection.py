import bluetooth

# Define the Bluetooth socket parameters
server_socket = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
port = 1 # RFCOMM port number
server_socket.bind(("", bluetooth.PORT_ANY))
server_socket.listen(1) # Maximum number of queued connections

# Wait for a Bluetooth client to connect
print("Waiting for a Bluetooth client...")
client_socket, client_address = server_socket.accept()
print(f"Accepted connection from {client_address}")

# Loop to receive commands from the client and send a response
while True:
    # Receive data from the client
    data = client_socket.recv(1024)
    if not data:
        # Connection has been closed by the client
        break
    
    # Convert received data to string and print it
    command = data.decode()
    print(f"Received command: {command}")
    
    # Perform some action based on the received command
    if command == "start":
        print("command start")
        # Add code here to control the mbot to move forward
    elif command == "forward":
        print("Moving forward...")
        # Add code here to control the mbot to move back    
    elif command == "back":
        print("Moving back...")
        # Add code here to control the mbot to move back
    elif command == "left":
        print("Turning left...")
        # Add code here to control the mbot to turn left
    elif command == "right":
        print("Turning right...")
        # Add code here to control the mbot to turn right
    else:
        print("Unknown command.")
    
    # Send a response to the client
    response = "Command received: " + command
    client_socket.send(response.encode())

# Close the sockets
client_socket.close()
server_socket.close()
