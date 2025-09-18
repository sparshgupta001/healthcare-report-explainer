from flask import Flask, request, jsonify
import fitz  # PyMuPDF
from analyzer import analyze_text

app = Flask(__name__)

@app.route("/analyze", methods=["POST"])
def analyze():
    if "file" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400
    
    file = request.files["file"]
    text = ""

    # Extract text from PDF
    with fitz.open(stream=file.read(), filetype="pdf") as pdf:
        for page in pdf:
            text += page.get_text()

    results = analyze_text(text)
    return jsonify(results)

if __name__ == "__main__":
    app.run(debug=True)
