import sys
sys.path.append('/home/admin/.local/lib/python3.9/site-packages')
from bluetooth_connection import BluetoothConnection
from serial_communication import SerialCommunication
import threading
from queue import Queue

# Initialize a queue for passing data between threads
data_queue = Queue()

# Initialize both threads
bt_thread = BluetoothConnection(data_queue)
serial_thread = SerialCommunication('/dev/ttyUSB0')

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
