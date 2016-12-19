from flask import Flask
from flask import request
import RaspberrySystem as rpi

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Tyagi IoT'


@app.route('/lamp', methods=['GET'])
def get_lamp():
    input_request = request.args.get('lamp')
    print('request->' + str(input_request))
    if 'ON' in input_request:
        # set LAMP ON
        rpi.set_lamp_on()
        response = 'LAMP ON'
        print('LAMP --> ' + response)
    elif 'OFF' in input_request:
        # set LAMP OFF
        rpi.set_lamp_off()
        response = 'LAMP OFF'
        print('LAMP --> ' + response)
    elif 'status' in input_request:
        # send LDR status
        print('Checking LDR STATUS...')
        response = '' + rpi.get_ldr_status()
        print('LDR STATUS--> ' + response)
    return response


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000);
