import serial
import api_requests
from threading import Thread
from Camera import *
import re
from picamera2 import Picamera2

def contains_digits(s):
    return any(c.isdigit() for c in s)

class SerialCommunication(Thread):
    def __init__(self, port):
        Thread.__init__(self)
        self.port = port
        self.ser = serial.Serial(self.port, 9600)
        self.latest_position = None

    def run(self):
        while True:
            if self.ser.in_waiting > 0:
                serial_data = self.ser.readline().decode('utf-8').strip()

                if serial_data == "TAKE_PICTURE":
                    def handle_take_picture():
                        image_data = capture_image_data()
                        api_requests.upload_avoided_collision(image_data)

                    take_picture_thread = Thread(target=handle_take_picture)
                    take_picture_thread.start()
                    
                elif contains_digits(serial_data):
                    x, y = self.extract_coordinates(serial_data)
                    api_requests.update_mower_position(x, y)
                    
                else:
                    print(serial_data)

    def extract_coordinates(self, message):
        x_pattern = r"X:\s*(-?\d+(\.\d+)?)"
        y_pattern = r"Y:\s*(-?\d+(\.\d+)?)" 

        x_match = re.search(x_pattern, message)
        y_match = re.search(y_pattern, message)

        x = float(x_match.group(1)) if x_match else None
        y = float(y_match.group(1)) if y_match else None

        return x, y
