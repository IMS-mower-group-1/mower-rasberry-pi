import serial
from picamera2 import Picamera2

picam2 = Picamera2()
ser = serial.Serial("/dev/ttyUSB0", 9600) 

try:
    ser = serial.Serial(port = "/dev/ttyUSB0", 
    baudrate = 9600,
    timeout = 0.1,
    parity = serial.PARITY_NONE,
    stopbits = serial.STOPBITS_ONE,
    bytesize = serial.EIGHTBITS)
    if ser.isOpen():
        print("Port is open")
    else:
        ser.open()
        print("Port was closed and is now open")

except serial.SerialException as e:
    print("Failed to open port: {}".format(e))

while True:
    signal = ser.readline().decode().strip()  # read the signal from the serial port
    print("Signal is: ",signal)
    if signal == "1":
        try:
            picam2.start_and_capture_file("test.jpg", delay=3, show_preview=False)
            print('Picture taken successfully!')
        except Exception as e:
            print('Error taking picture:', e)
    else:
        print("gotten other than 1")
    
    
        
