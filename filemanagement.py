import os
from operator import itemgetter
import glob
import logging


def keeponefile():
    try:
        ROOT_DIR = os.path.dirname(os.path.abspath("answer_file.json"))
        path = ROOT_DIR
        json_files = glob.glob(path + "/*.json", recursive=True)
        fileData = {}
        for fname in json_files:
            if "payload" in fname:
                fileData[fname] = os.stat(fname).st_mtime
                print(fname)

        sortedFiles = sorted(fileData.items(), key=itemgetter(0), reverse=True)
        print(sortedFiles)

        delete = len(sortedFiles)
        for x in range(0, delete):
            os.remove(sortedFiles[x][0])
    except Exception as e:
        logging.warning(f"Error in filemanagement.py = {e}")
