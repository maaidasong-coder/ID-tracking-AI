from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>ID Tracking AI is Running 🚀</h1><p>Welcome to your Flask deployment!</p>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
