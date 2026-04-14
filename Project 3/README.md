# MP3: MBTA Stop Finder

A Flask web app that helps you find the 3 nearest MBTA stops to any
Boston-area location. Enter a place name or address, and the app
geocodes it using the Mapbox API, finds the closest MBTA stops using
the MBTA V3 API, and displays them on an interactive map.

## Screenshots

### Home Page
![Home Page](screenshots/home.png)

### Results Page
![Results Page](screenshots/results.png)

### Map with Pins
![Map with Pins](screenshots/map.png)

## Project Structure

```
Project 3/
├── app.py              # Flask routes
├── mbta_helper.py      # Mapbox + MBTA API logic
├── .env                # API keys (not committed)
├── .gitignore          # Excludes .env from git
├── README.md           # This file
├── screenshots/        # Screenshots for README
├── templates/
│   ├── index.html      # Search form
│   └── result.html     # Results page with map
└── static/
    └── style.css       # Styling
```

## Setup Instructions

### 1. Clone the Repository

```
git clone https://github.com/ricguan1/oim3640.git
cd "Project 3"
```

### 2. Install Dependencies

```
pip install flask requests python-dotenv
```

### 3. Get API Keys

You will need two free API keys:

- **Mapbox**: Sign up at [mapbox.com](https://mapbox.com) and copy
your default public token from the account dashboard.
- **MBTA**: Register at [api-v3.mbta.com](https://api-v3.mbta.com)
and copy your API key from the confirmation email.

### 4. Configure Environment Variables

Create a file named `.env` in the Project 3 folder:

```
MAPBOX_TOKEN=your_mapbox_token_here
MBTA_API_KEY=your_mbta_key_here
```

Never commit this file — it is already excluded via `.gitignore`.

### 5. Run the App

```
python app.py
```

Then open your browser and go to `http://127.0.0.1:5000`

## How It Works

1. User enters a Boston-area place name or address into the search form
2. App sends the input to the Mapbox Geocoding API to get latitude and longitude
3. Coordinates are passed to the MBTA V3 API to find the nearest stops
4. Results are displayed with stop names, wheelchair accessibility, and an interactive map

## APIs Used

- [Mapbox Geocoding API](https://docs.mapbox.com/api/search/geocoding/)
- [MBTA V3 API](https://api-v3.mbta.com)

## WOW Factor

Instead of showing just one nearest stop, the app displays the 3
nearest MBTA stops. It prioritizes rail stops (subway, Green Line,
commuter rail) first, and falls back to include bus stops when fewer
than 3 rail stops are nearby — giving accurate results across both
urban and suburban Boston.