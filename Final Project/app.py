from flask import Flask, render_template, request
from nhl_helper import search_player, get_player_stats

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    results = []
    error = None
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        if name:
            try:
                results = search_player(name)
            except Exception:
                error = "Could not reach the NHL API. Please try again."
    return render_template("index.html", results=results, error=error)


@app.route("/player/<int:player_id>")
def player(player_id):
    try:
        stats = get_player_stats(player_id)
    except Exception:
        return render_template("index.html", results=[], error="Player not found.")
    return render_template("player.html", stats=stats)


if __name__ == "__main__":
    app.run(debug=True)