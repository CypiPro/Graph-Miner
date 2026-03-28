import webview
import os
import shutil

import cv2
import numpy as np

# Import own functionality
from modules import export, image_utils # add new modules if necessary

class Api:
    """
    This class serves as a communication layer between HTML and Python.
    No processing should be done here directly (only call necessary functions when invoked by JS). 
    """

    def save_temp_image(self, bytes, filename):
        return image_utils.save_temp_image(bytes, filename)



def exit_cleanup():
    # Program exit temporary file cleanup
    if os.path.isdir("temp"):
        shutil.rmtree("temp")


if __name__ == "__main__":
    webview.create_window (
        "Graph Miner",
        "ui/index.html",
        js_api = Api()
    )

    os.makedirs("temp", exist_ok=True)
    webview.start()
    exit_cleanup()