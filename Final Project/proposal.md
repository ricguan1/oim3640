# Final Project Proposal

## What are you building?

A Flask web app that lets users search for any NHL player by name and view their current season stats, career highlights, and recent game performance. Users can also compare two players side by side to see how they stack up.

## Why?

I follow hockey closely and found myself constantly jumping between different sites to look up player stats before games. This app puts everything in one place with a clean interface. It also builds directly on what I built in MP2 (data analysis and visualization) and MP3 (Flask web app with API integration), so I can apply everything I've learned in a domain I actually care about.

## MVP vs. Stretch Goals

**MVP (minimum working version):**
- Search any NHL player by name
- Display current season stats (goals, assists, points, games played)
- Simple bar chart or table visualization of key stats
- Clean Flask frontend with a search form and results page

**Stretch Goals (if time allows):**
- Compare two players side by side
- View upcoming game schedules by team
- AI-generated "scouting report" using the Claude API summarizing a player's season

## What don't I know yet?

- How the NHL Web API structures its player search endpoint and whether name search is supported directly or requires a player ID lookup first
- How to handle players with the same name in search results
- Best way to structure the Flask app to keep `app.py` clean while handling multiple API calls
- If I pursue the AI stretch goal, how to integrate the Claude API into a Flask route effectively
