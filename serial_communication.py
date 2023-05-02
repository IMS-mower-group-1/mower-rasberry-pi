import serial
from threading import Thread

class SerialCommunication(Thread):
    def __init__(self, port):
        Thread.__init__(self)
        self.port = port
        self.ser = serial.Serial(self.port, 9600)

    def run(self):
        while True:
            if self.ser.in_waiting > 0:
                serial_data = self.ser.readline().decode('utf-8').strip()
                print(f"Serial data received: {serial_data}")
