## My Project Proposal

**What I'm building:** A text analyzer that compares post-game interview 
transcripts from 3-5 NHL players to measure vocabulary size, most-used 
words, and repeated filler phrases.

**Why I chose this:** NHL players are notorious for giving robotic, 
repetitive post-game interviews. I want to find out if that's actually 
true — and if some players are worse than others.

**Core features:**
- Load and read transcript `.txt` files for multiple players
- Count word frequencies using a dictionary
- Clean text (lowercase, remove punctuation, remove filler stop words)
- Rank players by vocabulary richness (unique words / total words)
- Identify each player's most-used "signature" words and phrases

**What I don't know yet:**
- Where to find transcripts long enough to be meaningful
- How to remove common stop words ("the", "a", "I") without 
  losing useful data
- How to measure vocabulary "richness" beyond just counting unique words
- Whether the patterns I expect to find actually exist in the data