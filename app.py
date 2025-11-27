from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"message": "ZipGo Flask service running on port 5000"})

@app.route("/health")
def health():
    return jsonify({"status": "OK"})

if __name__ == "__main__":
    # Important: host=0.0.0.0 so Docker can expose it
    app.run(host="0.0.0.0", port=12120)
