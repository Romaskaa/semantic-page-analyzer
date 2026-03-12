import os

UPLOAD_DIR = "storage/uploads"

def save_file(file):

    path = os.path.join(UPLOAD_DIR, file.filename)

    with open(path, "wb") as f:
        f.write(file.file.read())

    return path