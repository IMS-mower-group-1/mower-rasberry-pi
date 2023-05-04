import io
import picamera
import time
from PIL import Image

def capture_image_data():
    with picamera.PiCamera() as camera:
        # Configure the camera settings if needed
        camera.resolution = (1024, 768)

        # Give the camera some time to adjust settings
        camera.start_preview()
        time.sleep(1)
        camera.stop_preview()

        # Capture the image into a BytesIO object
        with io.BytesIO() as image_data:
            camera.capture(image_data, 'jpeg')
            image_data.seek(0)

            # Load the image using PIL and rotate it
            image = Image.open(image_data)
            rotated_image = image.rotate(180, expand=True)

            # Save the rotated image into a new BytesIO object
            with io.BytesIO() as rotated_image_data:
                rotated_image.save(rotated_image_data, 'jpeg')
                rotated_image_data.seek(0)

                # Return the rotated image data
                return rotated_image_data.getvalue()
	


