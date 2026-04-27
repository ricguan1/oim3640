import requests

def format_season(season_id):
    s = str(season_id)
    return f"{s[:4]}-{s[6:]}"

SEARCH_URL = "https://search.d3.nhle.com/api/v1/search/player"
PLAYER_URL = "https://api-web.nhle.com/v1/player/{}/landing"

TEAM_COLORS = {
    "ANA": "#F47A38", "ARI": "#8C2633", "BOS": "#FFB81C", "BUF": "#003087",
    "CGY": "#CE1126", "CAR": "#CC0000", "CHI": "#CF0A2C", "COL": "#6F263D",
    "CBJ": "#002654", "DAL": "#006847", "DET": "#CE1126", "EDM": "#FF4C00",
    "FLA": "#041E42", "LAK": "#111111", "MIN": "#154734", "MTL": "#AF1E2D",
    "NSH": "#FFB81C", "NJD": "#CE1126", "NYI": "#F47D30", "NYR": "#0038A8",
    "OTT": "#E31837", "PHI": "#F74902", "PIT": "#FCB514", "SEA": "#99D9D9",
    "SJS": "#006D75", "STL": "#002F87", "TBL": "#002868", "TOR": "#003E7E",
    "UTA": "#71AFE5", "VAN": "#00843D", "VGK": "#B4975A", "WSH": "#041E42",
    "WPG": "#004C97", "NYI": "#F47D30", "MLK": "#111111",
}


def get_team_color(abbrev):
    return TEAM_COLORS.get(abbrev, "#003087")

def search_player(name):
    seen = set()
    results = []
    queries = [name]
    parts = name.strip().split()
    if len(parts) > 1:
        queries.append(parts[0])
        queries.append(parts[-1])

    for query in queries:
        params = {
            "culture": "en-us",
            "limit": 20,
            "q": query,
        }
        response = requests.get(SEARCH_URL, params=params)
        response.raise_for_status()
        players = response.json()
        for player in players:
            pid = int(player["playerId"])
            if pid not in seen:
                seen.add(pid)
                results.append({
                    "id": pid,
                    "name": player["name"],
                    "team": player.get("teamAbbrev") or "N/A",
                    "position": player.get("positionCode", "N/A"),
                    "active": player.get("active", False),
                })
    return results


def get_player_stats(player_id):
    url = PLAYER_URL.format(player_id)
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()

    bio = {
        "name": f"{data['firstName']['default']} {data['lastName']['default']}",
        "team": data.get("fullTeamName", {}).get("default", "N/A"),
        "position": data.get("position", "N/A"),
        "number": data.get("sweaterNumber", "N/A"),
        "headshot": data.get("headshot", ""),
        "birth_date": data.get("birthDate", "N/A"),
        "birth_city": data.get("birthCity", {}).get("default", "N/A"),
        "birth_country": data.get("birthCountry", "N/A"),
        "height": data.get("heightInInches", "N/A"),
        "weight": data.get("weightInPounds", "N/A"),
        "team_color": get_team_color(data.get("currentTeamAbbrev", "")),
    }

    current = data.get("featuredStats", {}).get("regularSeason", {}).get("subSeason", {})
    career = data.get("careerTotals", {}).get("regularSeason", {})
    last5 = data.get("last5Games", [])

    nhl_seasons = [
        s for s in data.get("seasonTotals", [])
        if s.get("leagueAbbrev") == "NHL" and s.get("gameTypeId") == 2
    ]
    for s in nhl_seasons:
        s["season_display"] = format_season(s["season"])

    return {
        "bio": bio,
        "current_season": current,
        "career": career,
        "last5": last5,
        "nhl_seasons": nhl_seasons,
    }


if __name__ == "__main__":
    print("Searching for 'mcdavid'...")
    results = search_player("mcdavid")
    for r in results:
        print(r)

    print("\nFetching stats for Connor McDavid (8478402)...")
    stats = get_player_stats(8478402)
    print("Name:", stats["bio"]["name"])
    print("Team:", stats["bio"]["team"])
    print("Current season points:", stats["current_season"].get("points"))
    print("Career points:", stats["career"].get("points"))
    print("Last 5 games:")
    for game in stats["last5"]:
        print(f"  {game['gameDate']} vs {game['opponentAbbrev']}: {game['goals']}G {game['assists']}A")

def get_scores_today():
    url = "https://api-web.nhle.com/v1/score/now"
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    games = []
    for game in data.get("games", []):
        games.append({
            "home": game.get("homeTeam", {}).get("abbrev", ""),
            "away": game.get("awayTeam", {}).get("abbrev", ""),
            "home_score": game.get("homeTeam", {}).get("score", 0),
            "away_score": game.get("awayTeam", {}).get("score", 0),
            "state": game.get("gameState", ""),
            "period": game.get("periodDescriptor", {}).get("number", ""),
            "home_logo": game.get("homeTeam", {}).get("logo", ""),
            "away_logo": game.get("awayTeam", {}).get("logo", ""),
        })
    return games


def get_category_leaders(category):
    url = f"https://api-web.nhle.com/v1/skater-stats-leaders/20252026/2?limit=10&categories={category}"
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    players = data.get(category, [])
    results = []
    for player in players:
        results.append({
            "name": f"{player.get('firstName', {}).get('default', '')} {player.get('lastName', {}).get('default', '')}",
            "team": player.get("teamAbbrev", ""),
            "value": player.get("value", 0),
            "headshot": player.get("headshot", ""),
            "id": player.get("id", 0),
        })
    return results


def get_scoring_leaders():
    return {
        "points": get_category_leaders("points"),
        "goals": get_category_leaders("goals"),
        "assists": get_category_leaders("assists"),
    }