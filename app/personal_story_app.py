from flask import Flask, request, render_template
import threading
import os

app = Flask(__name__)

request_counter = {"counter": 0}
lock = threading.Lock()


@app.route("/", methods=["GET", "POST"])
def index():
    story = ""

    with lock:
        request_counter["counter"] += 1
        count = request_counter["counter"]

    if count == 5:
        os._exit(1)
    
    if request.method == "POST":
        name = request.form["name"]
        hobbies = request.form["hobbies"]
        story = f"Hello - {name} who likes {hobbies}.\nThe LLMs were too heavy and it's really not about llms."
    return render_template("index.html", story=story)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, use_reloader=False)
