from picamera2 import Picamera2

picam2 = Picamera2()
picam2.start_and_capture_file("test.jpg", delay=3, show_preview=False)



