from flask import Flask, request, render_template

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    story = ""
    if request.method == "POST":
        name = request.form["name"]
        hobbies = request.form["hobbies"]
        story = f"Hello - {name} who likes {hobbies}.\nThe LLMs were too heavy and it's really not about llms."
    return render_template("index.html", story=story)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
