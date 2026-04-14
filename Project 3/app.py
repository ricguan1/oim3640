from flask import Flask, render_template, request
from mbta_helper import find_stops_near

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/nearest", methods=["POST"])
def nearest():
    place_name = request.form["place_name"]
    try:
        stops, lat, lng = find_stops_near(place_name)
        return render_template("result.html", stops=stops, place=place_name, lat=lat, lng=lng)
    except Exception:
        return render_template("index.html", error=f"Could not find MBTA stops near '{place_name}'. Try a different location.")


if __name__ == "__main__":
    app.run(debug=True)