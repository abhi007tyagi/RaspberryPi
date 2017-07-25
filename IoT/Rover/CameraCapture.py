import pygame
import pygame.camera
import time

import argparse
import base64

from googleapiclient import discovery
from oauth2client.client import GoogleCredentials


def capture_image(file):
    pygame.camera.init()
    pygame.camera.list_cameras()
    cam = pygame.camera.Camera("/dev/video0", (640, 480))
    cam.start()
    time.sleep(0.1)  # You might need something higher in the beginning
    img = cam.get_image()
    if file:
        pygame.image.save(img, file)
    else:
        pygame.image.save(img, "img_captured.jpg")
    cam.stop()


def main():
    credentials = GoogleCredentials.get_application_default()
    service = discovery.build('vision', 'v1', credentials=credentials)

    with open('img_captured.jpg', 'rb') as image:
        image_content = base64.b64encode(image.read())
        service_request = service.images().annotate(body={
            'requests': [{
                'image': {
                    'content': image_content.decode('UTF-8')
                },
                'features': [{
                    'type': 'LOGO_DETECTION',
                    'maxResults': 1
                }]
            }]
        })
        response = service_request.execute()

        try:
            label = response['responses'][0]['logoAnnotations'][0]['description']
        except:
            label = "No response."

        print("Detected -->" + label)


if __name__ == '__main__':
    main()