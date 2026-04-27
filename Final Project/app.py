import io
import base64
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from flask import Flask, render_template, request
from nhl_helper import search_player, get_player_stats
from nhl_helper import search_player, get_player_stats, get_scores_today, get_scoring_leaders

app = Flask(__name__)


def build_points_chart(nhl_seasons, team_color="#111111"):
    seasons = [s["season_display"] for s in nhl_seasons]
    points = [s.get("points", 0) for s in nhl_seasons]

    fig, ax = plt.subplots(figsize=(10, 4))
    ax.bar(seasons, points, color=team_color)
    ax.set_title("Points Per Season", fontsize=14, color="#111111")
    ax.set_xlabel("Season")
    ax.set_ylabel("Points")
    ax.tick_params(axis="x", rotation=45)
    for i, v in enumerate(points):
        ax.text(i, v + 1, str(v), ha="center", va="bottom", fontsize=8, color="#111111")
    plt.tight_layout()

    buf = io.BytesIO()
    plt.savefig(buf, format="png")
    buf.seek(0)
    chart = base64.b64encode(buf.read()).decode("utf-8")
    plt.close()
    return chart

def build_compare_chart(stats1, stats2):
    name1 = stats1["bio"]["name"]
    name2 = stats2["bio"]["name"]
    color1 = stats1["bio"]["team_color"]
    color2 = stats2["bio"]["team_color"]
    categories = ["Goals", "Assists", "Points"]
    vals1 = [
        stats1["current_season"].get("goals", 0),
        stats1["current_season"].get("assists", 0),
        stats1["current_season"].get("points", 0),
    ]
    vals2 = [
        stats2["current_season"].get("goals", 0),
        stats2["current_season"].get("assists", 0),
        stats2["current_season"].get("points", 0),
    ]

    x = range(len(categories))
    width = 0.35
    fig, ax = plt.subplots(figsize=(8, 4))
    bars1 = ax.bar([i - width/2 for i in x], vals1, width, label=name1, color=color1)
    bars2 = ax.bar([i + width/2 for i in x], vals2, width, label=name2, color=color2)

    for bar in bars1:
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.5,
                str(int(bar.get_height())), ha="center", va="bottom", fontsize=9, color=color1)
    for bar in bars2:
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.5,
                str(int(bar.get_height())), ha="center", va="bottom", fontsize=9, color=color2)

    ax.set_xticks(list(x))
    ax.set_xticklabels(categories)
    ax.set_title("Current Season Comparison", fontsize=13, color="#111111")
    ax.legend()
    plt.tight_layout()

    buf = io.BytesIO()
    plt.savefig(buf, format="png")
    buf.seek(0)
    chart = base64.b64encode(buf.read()).decode("utf-8")
    plt.close()
    return chart

@app.route("/", methods=["GET", "POST"])
def index():
    results = []
    error = None
    selected_filter = "all"
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        selected_filter = request.form.get("filter", "all")
        if name:
            try:
                results = search_player(name)
                if selected_filter == "active":
                    results = [p for p in results if p["active"]]
                elif selected_filter == "inactive":
                    results = [p for p in results if not p["active"]]
            except Exception:
                error = "Could not reach the NHL API. Please try again."
    return render_template("index.html", results=results, error=error, selected_filter=selected_filter)


@app.route("/player/<int:player_id>")
def player(player_id):
    try:
        stats = get_player_stats(player_id)
    except Exception:
        return render_template("index.html", results=[], error="Player not found.")
    chart = build_points_chart(stats["nhl_seasons"], stats["bio"]["team_color"])
    return render_template("player.html", stats=stats, chart=chart)


@app.route("/compare", methods=["GET", "POST"])
def compare():
    results1 = []
    results2 = []
    error = None
    name1 = ""
    name2 = ""
    if request.method == "POST":
        name1 = request.form.get("name1", "").strip()
        name2 = request.form.get("name2", "").strip()
        try:
            if name1:
                results1 = [p for p in search_player(name1) if p["active"]]
            if name2:
                results2 = [p for p in search_player(name2) if p["active"]]
        except Exception:
            error = "Could not reach the NHL API. Please try again."
    return render_template("compare.html", results1=results1, results2=results2,
                           name1=name1, name2=name2, error=error)


@app.route("/compare/<int:id1>/<int:id2>")
def compare_players(id1, id2):
    try:
        stats1 = get_player_stats(id1)
        stats2 = get_player_stats(id2)
    except Exception:
        return render_template("compare.html", results1=[], results2=[],
                               name1="", name2="", error="Could not load player data.")
    chart = build_compare_chart(stats1, stats2)
    return render_template("compare_result.html", stats1=stats1, stats2=stats2, chart=chart)

@app.route("/leaders")
def leaders():
    try:
        scores = get_scores_today()
        scoring_leaders = get_scoring_leaders()
    except Exception as e:
        scores = []
        scoring_leaders = {"points": [], "goals": [], "assists": []}
    return render_template("leaders.html", scores=scores, leaders=scoring_leaders)

if __name__ == "__main__":
    app.run(debug=True)