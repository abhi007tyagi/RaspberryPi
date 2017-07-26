import base64
import os
import CameraCapture as cam

from googleapiclient import discovery
from oauth2client.client import GoogleCredentials


def main():
    cam.capture_image("image_captured.jpg")
    credentials = GoogleCredentials.get_application_default()
    service = discovery.build('vision', 'v1', credentials=credentials)

    with open('image_captured.jpg', 'rb') as image:
        image_content = base64.b64encode(image.read())
        service_request = service.images().annotate(body={
            'requests': [{
                'image': {
                    'content': image_content.decode('UTF-8')
                },
                'features': [{
                    'type': 'TEXT_DETECTION',
                    'maxResults': 1
                }]
            }]
        })
        response = service_request.execute()
        # print json.dumps(response, indent=4, sort_keys=True)	#Print it out and make it somewhat pretty.
        try:
            label = response['responses'][0]['textAnnotations'][0]['description']
            label = label.rstrip()
        except:
            label = "No response."

        print(label)
        cmd = 'espeak "{0}" 2>/dev/null'.format(label)
        os.system(cmd)


if __name__ == '__main__':
    main()