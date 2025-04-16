import sys
from flask import Flask, render_template, request
import json
from app.analyzer import parse_policy
from app.visualizer import generate_mermaid_graph

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    graph = ""
    error = ""

    if request.method == "POST":
        file = request.files.get("policy_file")
        if file and file.filename.endswith(".json"):
            try:
                policy = json.load(file)
                parsed = parse_policy(policy)
                graph = generate_mermaid_graph(parsed)
            except Exception as e:
                error = f"Failed to parse policy: {str(e)}"
        else:
            error = "Please upload a valid JSON file."

    return render_template("index.html", graph=graph, error=error)

if __name__ == "__main__":
    app.run(debug=True)
