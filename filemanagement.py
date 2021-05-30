import os
from operator import itemgetter
import glob
import logging


def keeponefile():
    try:
        ROOT_DIR = os.path.dirname(os.path.abspath("answer_file.json"))
        json_files = glob.glob(ROOT_DIR + "/*.json", recursive=True)
        for fname in json_files:
            if "payload" in fname:
                os.remove(fname)
    except Exception as e:
        logging.warning(f"Error in filemanagement.py = {e}")
