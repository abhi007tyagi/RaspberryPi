from datetime import timedelta
from flask import Flask, make_response, request, current_app, jsonify
from functools import update_wrapper
import requests
import HTMLStripper
import CarControl as car


app = Flask(__name__)


def crossdomain(origin=None, methods=None, headers=None,
                max_age=21600, attach_to_all=True,
                automatic_options=True):
    if methods is not None:
        methods = ', '.join(sorted(x.upper() for x in methods))
    if headers is not None and not isinstance(headers, str):
        headers = ', '.join(x.upper() for x in headers)
    if not isinstance(origin, str):
        origin = ', '.join(origin)
    if isinstance(max_age, timedelta):
        max_age = max_age.total_seconds()

    def get_methods():
        if methods is not None:
            return methods

        options_resp = current_app.make_default_options_response()
        return options_resp.headers['allow']

    def decorator(f):
        def wrapped_function(*args, **kwargs):
            if automatic_options and request.method == 'OPTIONS':
                resp = current_app.make_default_options_response()
            else:
                resp = make_response(f(*args, **kwargs))
            if not attach_to_all and request.method != 'OPTIONS':
                return resp

            h = resp.headers

            h['Access-Control-Allow-Origin'] = origin
            h['Access-Control-Allow-Methods'] = get_methods()
            h['Access-Control-Max-Age'] = str(max_age)
            if headers is not None:
                h['Access-Control-Allow-Headers'] = headers
            return resp

        f.provide_automatic_options = False
        return update_wrapper(wrapped_function, f)

    return decorator


@app.route('/')
def hello_jarvis():
    return 'Test is up and running'


@app.route('/gnip', methods=['GET', 'POST', 'OPTIONS'])
@crossdomain(origin="*", headers=['Content-Type', 'Accept'])
def gnip_connect():
    try:
        input_request = request.get_json(silent=True)
        print("request in -->" + str(input_request))
        question = input_request['result']['resolvedQuery']
        print("question -->", question)

        url = 'https://ai.genpact.com:9906/gnip172classifier/neural-chat/getResults'
        data = '{"query":"' + question + '"}'
        print("gnip data->" + data)

        headers = {'Content-Type': 'application/json'}

        resp = requests.post(url, data=data, headers=headers)
        resultjson = resp.json()
        print("gnip response->" + str(resultjson))

        result = HTMLStripper.strip_tags(resultjson['result'][0]['answer'])

        print("gnip result->" + result)
    except Exception as e:
        print("Error -->",e)
        result = ""

    print("Result --> ", result)
    resp = jsonify(
        speech=result,
        source="gnip",
        displayText=result
    )

    print("Server Response --> ", resp)
    return resp


@app.route('/carcontrol', methods=['GET'])
@crossdomain(origin="*", headers=['Content-Type', 'Accept'])
def car_control():
    try:
        action = request.args.get('action')
        print("gnip action ->" + action)

        if str(action) == "FW'":
            print("detected action FW")
            car.on_control("FW")
        elif str(action) == "BW'":
            print("detected action BW")
            car.on_control("BW")
        elif str(action) == "LT'":
            print("detected action LT")
            car.on_control("LT")
        elif str(action) == "RT'":
            print("detected action RT")
            car.on_control("RT")
        elif str(action) == "ST'":
            print("detected action ST")
            car.on_control("ST")

    except Exception as e:
        print("Error -->", e)

    return "OK"


if __name__ == '__main__':
    app.run()
