from model import ToxicModel
from flask import Flask, request, jsonify

# Setup
model = ToxicModel()
app = Flask(__name__, )

@app.route("/", methods=["GET"])
def main():
    message = request.get_json()["message"]
    pred = model.predict(message)
    out = {k:str(v) for k, v in pred.items()}
    return out


app.run()