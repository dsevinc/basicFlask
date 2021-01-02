from flask import Flask, jsonify, request, render_template, make_response
import time
from conversion import *
app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    if (request.method == 'POST'):
        some_json = request.get_json()
        return jsonify({'sent': some_json}), 201
    else:
        return jsonify({"about":"hello world!"})

@app.route('/multi/<int:num>', methods=['GET'])
def get_multiply10(num):
    return jsonify({"result":num*10})

@app.route('/hello/<name>', methods=['GET'])
def hello(name):
    headers = {'Content-Type': 'text/html'}
    return make_response(render_template('hello.html', name=name), 200, headers)

@app.route('/time')
def get_current_time():
    return jsonify({"time":time.time()})

@app.route('/convertUnit', methods=['GET'])
def convertUnit():
    inputUnit = request.args.get('inputUnit',None)
    outputUnit = request.args.get('outputUnit',None)
    inputValue = request.args.get('inputValue',None)

    if (inputUnit in si_units and outputUnit in si_units):
        outValue = convert_SI_units(inputUnit, outputUnit, float(inputValue))
    elif (inputUnit in si_units and outputUnit in imperial_units):
        outValue = convert_SI_to_imperial(inputUnit, outputUnit, float(inputValue))
    elif (inputUnit in imperial_units and outputUnit in si_units):
        outValue = convert_imperial_to_SI(inputUnit, outputUnit, float(inputValue))
    elif (inputUnit in imperial_units and outputUnit in imperial_units):
        outValue = convert_imperial_units(inputUnit, outputUnit, float(inputValue))
    else:
        outValue = "Error"

    return jsonify({"result":outValue})

if __name__ == '__main__':
    app.run(debug=True)