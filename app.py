from flask import Flask, jsonify, request
from weather import get_weather, get_forecast

app = Flask(__name__)

@app.route("/health")
def health():
    return jsonify({"status": "ok"})

@app.route("/weather/<city>")
def weather(city):
    data = get_weather(city)
    if data is None:
        return jsonify({"error": "City not found"}), 404
    return jsonify(data)

@app.route("/forecast/<city>")
def forecast(city):
    days = request.args.get("days", 3, type=int)
    data = get_forecast(city, days)
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True, port=5000)
