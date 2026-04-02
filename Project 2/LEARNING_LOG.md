# Learning Log - Mini Project 2

## What I Built
An NHL player interview analyzer that reads post-game transcript files,
counts word frequencies, and compares vocabulary richness across 
Connor McDavid, Sidney Crosby, and Auston Matthews.

## Concepts I Used

### Dictionaries & Counting Pattern
This project made the counting pattern click for me. Using 
`counts.get(word, 0) + 1` to build a frequency dictionary from 
scratch was something I had seen in class, but actually applying it 
to real interview data made it feel useful. I now understand why 
dictionaries are the right tool for this — you need to look up and 
update values by a meaningful key (the word), not by index.

### File I/O
I learned how to read real `.txt` files using `open()` and `.read()`. 
One thing that tripped me up was the file path — Python looks for 
files relative to where you run the script, not where the script 
lives. I fixed this by running the script from the correct directory.

### matplotlib Bar Charts
I had never used matplotlib before. I learned how to create 
subplots side by side using `plt.subplots()` and save the output 
as a `.png` file with `plt.savefig()`. Seeing the bar charts render 
from data I collected myself was satisfying.

## What Was Hard: Cleaning the Text
The hardest part was figuring out what to remove from the word counts.
The first pass showed words like "the", "and", "a" dominating every 
list — obvious stop words. But the trickier problem was transcript 
artifacts: YouTube auto-captions fused words together like 
"secondsyou" and "secondsand", which showed up as real words in the 
counts. I had to manually identify and add these to the STOP_WORDS 
set. This taught me that real-world text data is messy and cleaning 
it is an iterative process, not a one-time fix.

## What I Found
- Sidney Crosby has the highest vocabulary richness score (0.308)
- Connor McDavid is the most repetitive (0.240) and says "obviously" 
  as his signature word
- Auston Matthews uses hedging language like "think", "mean", 
  and "kind" most frequently

## What Surprised Me
I expected McDavid, the best player in the world, to be more 
articulate in interviews. The data showed the opposite — he was 
the most repetitive of the three. Crosby, the veteran, actually 
spoke with the most variety.

## What I Would Do Differently
If I had more time, I would find longer transcripts to make the 
vocabulary richness scores more reliable. I would also automate 
the stop word detection instead of manually adding words one by one.