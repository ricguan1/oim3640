# NHL Player Dashboard

A Flask web app that lets you search for any NHL player, view their stats, and compare two players side by side. Built using the NHL Web API with no API key required.

## What It Does

- Search any NHL player by name with active/inactive filtering
- View current season stats, last 5 games, and full career history
- See a points-per-season bar chart for any player
- Compare two players side by side with a current season stats table and visualization

## How to Run

### 1. Clone the repo
git clone https://github.com/ricguan1/oim3640.git
cd oim3640/Final\ Project

### 2. Install dependencies
pip install flask requests matplotlib

### 3. Run the app
python app.py

### 4. Open in your browser
http://127.0.0.1:5000

## Project Structure

Final Project/
├── app.py              # Flask routes and chart generation
├── nhl_helper.py       # NHL API functions
├── templates/
│   ├── index.html          # Search page
│   ├── player.html         # Player stats page
│   ├── compare.html        # Player comparison search
│   └── compare_result.html # Player comparison results
└── static/             # Static assets

## APIs Used

All data comes from the NHL Web API — no API key required.

- search.d3.nhle.com/api/v1/search/player — player name search
- api-web.nhle.com/v1/player/{id}/landing — player stats, bio, career history

## Requirements

- Python 3.x
- Flask
- requests
- matplotlib
