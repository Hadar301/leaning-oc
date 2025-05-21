from flask import Flask, request, render_template
from langchain.llms import LlamaCpp
import os

app = Flask(__name__)

# Load model only once
llm = LlamaCpp(
    model_path="app/models/mistral.gguf",
    n_ctx=2048,
    temperature=0.8,
    max_tokens=256,
    verbose=False
)

def generate_story(name, hobbies):
    prompt = f"Write a fun short story about a person named {name} who enjoys {hobbies}."
    try:
        return llm(prompt)
    except Exception as e:
        return f"Error: {e}"

@app.route("/", methods=["GET", "POST"])
def index():
    story = ""
    if request.method == "POST":
        name = request.form["name"]
        hobbies = request.form["hobbies"]
        story = generate_story(name, hobbies)
    return render_template("index.html", story=story)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
