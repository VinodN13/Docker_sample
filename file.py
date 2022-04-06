from flask import Flask
app = Flask(__name__)
print("test")
@app.route("/")
def hello():
    return "<h1 style='color:blue'>Good afternoon</h1>"
    print("hello")
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=3010)
