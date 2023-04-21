from api_requests import *
import serial

def handleSignal(signal):
    if signal == "start_mow_session":
        print("Arduino wants to start mow session")
    elif signal == "end_mow_session":
        print("Arduino wants to end mow session")
    elif signal == "take_picture":
        print("Arduino wants to take picture")
    else:
        print(f"Arduino wants to say the following unhandled thing: {signal}")

ser = serial.Serial("/dev/ttyUSB0", 9600)

try:
    ser = serial.Serial(port="/dev/ttyUSB0",
                        baudrate=9600,
                        timeout=0.1,
                        parity=serial.PARITY_NONE,
                        stopbits=serial.STOPBITS_ONE,
                        bytesize=serial.EIGHTBITS)
    if ser.isOpen():
        print("Port is open")
    else:
        ser.open()
        print("Port was closed and is now open")

except serial.SerialException as e:
    print("Failed to open port: {}".format(e))

while True:
    signal = ser.readline().decode().strip()  # read the signal from the serial port
    
    if len(signal) != 0:
        handleSignal(signal)
		

