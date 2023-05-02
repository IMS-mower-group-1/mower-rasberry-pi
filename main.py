import sys
sys.path.append('/home/admin/.local/lib/python3.9/site-packages')
from bluetooth_connection import BluetoothConnection
from serial_communication import SerialCommunication
import threading

# Initialize both threads
bt_thread = BluetoothConnection()
serial_thread = SerialCommunication('/dev/ttyUSB0')

# Start both threads
bt_thread.start()
serial_thread.start()

# Main program loop
while True:
    try:
        for data in bt_thread.run():
            serial_thread.ser.write(data.encode())
    except KeyboardInterrupt:
        bt_thread.join()
        serial_thread.join()
        break
