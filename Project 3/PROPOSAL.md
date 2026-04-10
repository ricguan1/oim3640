# My Project Proposal

**What I'm building:** A Flask web app that finds the 3 nearest MBTA 
stops from any Boston-area address or place name.

**Why I chose this:** Living near Boston, I often need to figure out 
which T stop is closest when going somewhere new — this solves that 
real problem.

**Core features:**
- User enters any place name or address
- App geocodes it using the Mapbox API
- Finds the 3 nearest MBTA stops using the MBTA V3 API
- Displays stop names and wheelchair accessibility for each
- Shows results on an interactive Mapbox map with pins

**What I don't know yet:**
- How to embed a Mapbox GL JS map inside a Flask HTML template
- How the MBTA API structures its response JSON
- How to display multiple stop markers on the same map
- How to handle errors when a place isn't found