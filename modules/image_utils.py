# Image loading/processing module
import os

def save_temp_image(bytes_data, filename):
    """Save uploaded file into temp folder"""

    path = os.path.join("temp", filename)

    with open(path, "wb") as f:
        f.write(bytes(bytes_data))

    return path