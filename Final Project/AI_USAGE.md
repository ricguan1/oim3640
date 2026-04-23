# AI Usage Documentation

This file documents my use of AI tools (Claude) during the development of this project.

## 1. Project Planning and Idea Selection

**What I asked:** I described several project ideas including an NHL stats dashboard, a ski resort tracker, and a flight tracker, and asked which would be most practical and demonstrable for a gallery walk.

**What AI generated:** A comparison of each idea's strengths and weaknesses, recommending the NHL dashboard for its broad appeal and interactive search capability.

**What I did with it:** I agreed with the recommendation and used it to finalize my project direction. The final decision was mine based on my own interest in hockey.

**What I learned:** Thinking about who your audience is matters when designing an app — a project built for others to demo needs to be immediately intuitive.

## 2. NHL API Research

**What I asked:** I asked which NHL API endpoints to use for player search and stats, and how to structure the data pipeline from name search to player ID to stats.

**What AI generated:** Identified two key endpoints — the search endpoint and the landing endpoint — and explained the two-step lookup process.

**What I did with it:** I tested both endpoints manually in my browser before writing any code to verify the data structure and confirm the fields I needed.

**What I learned:** Always test an API manually before writing code. Seeing the raw JSON first made it much easier to write the parser.

## 3. nhl_helper.py

**What I asked:** Asked for help writing two core functions: search_player() and get_player_stats().

**What AI generated:** Initial versions of both functions with basic parsing logic.

**What I did with it:** I ran the code, verified the output matched what I saw in the browser, and then modified the search function to fix a bug where players like Quinn Hughes were not appearing. I added a multi-query approach that searches by full name, first name, and last name separately and deduplicates results.

**What I learned:** API search endpoints often have relevance ranking quirks. Making multiple targeted queries and deduplicating is a practical workaround.

## 4. Flask App Structure

**What I asked:** Asked for help structuring app.py with routes for search, player stats, and player comparison.

**What AI generated:** The initial route structure and render_template calls.

**What I did with it:** I reorganized the file when a route placement bug caused an IndentationError, moving all routes above the if __name__ == "__main__" block. I also debugged a blank page issue caused by truncated HTML templates.

**What I learned:** Flask requires all routes to be defined before the app runs. The if __name__ == "__main__" block must always be last.

## 5. Data Visualization

**What I asked:** Asked how to generate a bar chart using matplotlib and embed it in a Flask template without saving to disk.

**What AI generated:** The build_points_chart() function using io.BytesIO and base64 encoding to serve the chart as an inline image.

**What I did with it:** I used the approach as-is and then extended it to build a second chart for the player comparison feature, adding side-by-side grouped bars with value labels.

**What I learned:** You can generate charts entirely in memory and serve them as base64 strings — no need to save files to disk. This is much cleaner for a web app.

## 6. Player Comparison Feature

**What I asked:** Asked for help building a two-player comparison page with search, selection, and a side-by-side stats table.

**What AI generated:** The compare.html and compare_result.html templates and two new Flask routes.

**What I did with it:** I debugged several issues including a JavaScript ReferenceError caused by template truncation during pasting, and a Jinja2 TemplateSyntaxError caused by inline tuple syntax in for loops. I rewrote the template to use explicit row-by-row HTML instead of a loop to fix the syntax error.

**What I learned:** Jinja2 has limitations with complex inline expressions. When a template throws a syntax error, breaking it into simpler explicit statements is more reliable than trying to write clever one-liners.

## 7. Season Formatting

**What I asked:** Asked how to format season IDs like 20152016 into readable labels like 2015-16.

**What AI generated:** A one-line format_season() function using string slicing.

**What I did with it:** Added it to nhl_helper.py and called it when building the nhl_seasons list so the display label is attached at the data layer, not the template layer.

**What I learned:** It is cleaner to format data in Python before passing it to a template rather than formatting it inside Jinja2.
ENDOFFILE