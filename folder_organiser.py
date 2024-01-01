import shutil
import os

try:
    os.mkdir("pdfs")
except FileExistsError:
    pass
try:
    os.mkdir("pics")
except FileExistsError:
    pass
try:
    os.mkdir("text")
except FileExistsError:
    pass
try:
    os.mkdir("videos")
except FileExistsError:
    pass

while True:
    files = os.listdir(path=".")
    for file in files:
        if file.endswith(".txt"):
            shutil.move(file, "text")
        elif file.endswith(".pdf"):
            shutil.move(file, "pdfs")
        elif file.endswith(".jpg"):
            shutil.move(file, "pics")
        elif file.endswith(".png"):
            shutil.move(file, "pics")
        elif file.endswith(".jpeg"):
            shutil.move(file, "pics")
        elif file.endswith(".mp4"):
            shutil.move(file, "videos")
        elif file.endswith(".mkv"):
            shutil.move(file, "videos")
        else:
            pass