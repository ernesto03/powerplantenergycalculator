from flask import jsonify, session, redirect, url_for
import json
from calculator_mw import calculator
import logging

def receive_file():
    try:

        """
        This function will read the payloadfile and verify if data is missing in the file.
        If payloadfile is correct, it will send it to be processed by another function.
        After successful processing, this function will write the files to the system
        and return the answerfile and/or errors.
        """
        # payload file is read and verified to see if data is missing
        payload_file = session["data"]
        with open(payload_file, "r") as pstr:
            received_payload_string = pstr.read()  # returns a string
        try:
            received_payload_dictionary = json.loads(received_payload_string)  # Give back a dictionnary
        except json.decoder.JSONDecodeError:
            errors = {"error": "Some of the data are missing or the name of the payload file may be wrong. Please "
                               "read the README.md file, verify the payload file and try again"}
            returndata = "/"
            return returndata, jsonify(errors)
        calculated_answer_string, errors = calculator(received_payload_dictionary)  # returns a string and a dictionary
        with open("answer_file.json", "w") as ptw:
            ptw.write(calculated_answer_string)
        calculated_answer = json.loads(calculated_answer_string)  # we make a list out of a string
        return jsonify(calculated_answer), jsonify(errors)  # we create a 'flask wrappers' json response
    except Exception as e:
        logging.warning(f"Exeption in build_json_file.py = {e}")
