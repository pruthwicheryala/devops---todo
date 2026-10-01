from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>My DevOps To-Do App</h1>
    <p>Hello! My first DevOps project is running 🚀</p>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

