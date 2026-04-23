import requests

SEARCH_URL = "https://search.d3.nhle.com/api/v1/search/player"
PLAYER_URL = "https://api-web.nhle.com/v1/player/{}/landing"


def search_player(name):
    params = {
        "culture": "en-us",
        "limit": 20,
        "q": name,
    }
    response = requests.get(SEARCH_URL, params=params)
    response.raise_for_status()
    players = response.json()
    results = []
    for player in players:
        results.append({
            "id": int(player["playerId"]),
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
    }

    current = data.get("featuredStats", {}).get("regularSeason", {}).get("subSeason", {})
    career = data.get("careerTotals", {}).get("regularSeason", {})
    last5 = data.get("last5Games", [])

    nhl_seasons = [
        s for s in data.get("seasonTotals", [])
        if s.get("leagueAbbrev") == "NHL" and s.get("gameTypeId") == 2
    ]

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