from flask import Flask, jsonify, request
from weather import get_weather, get_forecast, check_alerts

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

@app.route("/alerts/<city>")
def alerts(city):
    # No rate limiting, no input sanitisation
    result = check_alerts(city)
    return jsonify({"city": city, "alerts": result})

@app.route("/subscribe", methods=["POST"])
def subscribe():
    data = request.get_json()
    email = data["email"]  # No validation, will crash if missing
    city = data["city"]
    # Hardcoded timeout that should be configurable
    import time
    time.sleep(0.5)
    return jsonify({"status": "subscribed", "email": email, "city": city})

if __name__ == "__main__":
    app.run(debug=True, port=5000)
