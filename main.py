"""
Python3.8
Author: Ernest Lassman Kayembe
Name of application: main.py
Last updated: 29/05/2021
This application calculates the amount of energy each powerplant will produce.
To do that, the user must upload a specific payload_file.json document into the webpage.
It's important to add a payload_file.json with the same data as specified in the README.md file.
The application will make calculations and return an answer on screen.
If multiple browsers are connected to the same webpage endpoint /productionplan,
they will also be able to see the generated result.
"""
# Start with a basic flask app webpage.
import eventlet

eventlet.monkey_patch()
# It is recommended to apply eventlet at the top of the main scripts
from flask_socketio import SocketIO
from flask import Flask, render_template, request, session, jsonify
from threading import Thread, Event
import json
import os
from build_json_file import receive_file
from filemanagement import keeponefile
import logging

async_mode = "eventlet"
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
app.config['DEBUG'] = True

ROOT_DIR = os.path.dirname(os.path.abspath("answer_file.json"))
app.config["JSON_UPLOADS"] = ROOT_DIR

# turn the flask app into a socketio app
socketio = SocketIO(app, async_mode=async_mode, logger=True, engineio_logger=True)

# random number Generator Thread
thread = Thread()
thread_stop_event = Event()
logging.basicConfig(filename='appRuntimeMonitor.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')


# Created a function to access the /productionplan endpoint where we receive post requests
@app.route("/productionplan", methods=['POST', 'GET'])
def home():
    """
    This function creates the homepage as we see it.
    It verifies the posted data and sends it to other function for processing.
    After pcessing is done by other functions, this function will send data through the socket and
    show results on the screen.
    """
    try:
        if request.method == 'POST':
            keeponefile()
            # We add the newly uploaded file to the system for processing
            payload_json = request.files["payloadjson"]
            if "payload" in payload_json.filename:
                payload_json.save(os.path.join(app.config["JSON_UPLOADS"], payload_json.filename))
            # We verify if the name of the payload file is written as required and exists
            elif "payload" not in payload_json.filename:
                # We create an error response printed on the browser
                errordata = {
                    "newerror": "The filename is not correct or the file is missing, please read the README.md "
                                "file and try again."}
                socketio.emit('newerrorfiles', errordata, namespace='/showall', broadcast=True)
                logging.warning(f"User error = {errordata}")
                return jsonify(errordata)  # returns a 'flask wrapper' json response
            # We save the payload filename in the current session
            payload_filename = payload_json.filename
            # we save the payload filename in the session data
            session["data"] = payload_filename
            answerresponse, errors = receive_file()
            # We verify if an error was produced when processing the file
            if errors.get_json().get("error") != "Empty":
                logging.warning(f"User error = {errors.get_json().get('error')}")
                socketio.emit('newerrorfiles', {'newerror': errors.get_json().get("error")}, namespace='/showall',
                              broadcast=True)
                return errors
            else:
                # We use the payload filename from the sessiondata
                payload_filename = session["data"]
                payload_j = json.load(open(payload_filename))
                answer_j = json.load(open("answer_file.json"))
                # payload and answer files are both sent to the client via socket connection
                socketio.emit('newfiles', {"payload_j": payload_j, "answer_j": answer_j}, namespace='/showall',
                              broadcast=True)
                return answerresponse
        else:
            return render_template('index.html')
    except Exception as e:
        logging.warning(f"Error in main.py = {e}")


if __name__ == '__main__':
    socketio.run(app, debug=False, port=8888, host="0.0.0.0")
