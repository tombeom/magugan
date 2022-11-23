import os
from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

@app.route("/")
def home():
    with open("/home/magu/magugan/carCnt.txt", "r") as file:
        leftCount = file.readline()
    return render_template("front.html", leftCount = leftCount)

@app.route("/favicon.ico")
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),'favicon.ico')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port ="5000")