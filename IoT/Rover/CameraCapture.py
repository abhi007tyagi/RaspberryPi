import pygame
import pygame.camera


def capture_image(file):
    pygame.camera.init()
    pygame.camera.list_cameras()
    cam = pygame.camera.Camera("/dev/video0", (640, 480))
    cam.start()
    #time.sleep(0.1)  # You might need something higher in the beginning
    img = cam.get_image()
    if file:
        pygame.image.save(img, file)
    else:
        pygame.image.save(img, "img_captured.jpg")
    cam.stop()