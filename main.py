import sys
sys.path.append('/home/admin/.local/lib/python3.9/site-packages')
import time
from bluetooth_connection import BluetoothConnection
from serial_communication import SerialCommunication
import threading
from queue import Queue
import api_requests

# Initialize a queue for passing data between threads
data_queue = Queue()

# Initialize both threads
bt_thread = BluetoothConnection(data_queue)
serial_thread = SerialCommunication('/dev/ttyUSB0')

# Wait for wifi-connection to be established
time.sleep(10)

# Check if there is an active mow session
active_session_exists = api_requests.active_session_exists()
if active_session_exists:
	data_queue.put("START_SESSION")
else:
	data_queue.put("END_SESSION")
# Start both threads
bt_thread.start()
serial_thread.start()

# Main program loop
while True:
    try:
        if not data_queue.empty():
            data = data_queue.get()
            serial_thread.ser.write(data.encode())
    except KeyboardInterrupt:
        bt_thread.join()
        serial_thread.join()
        break
