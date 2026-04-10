# NHL Player Interview Analyzer

## What I Built
A Python program that analyzes post-game interview transcripts from 
3 NHL players to compare vocabulary richness and word patterns.

## Players Analyzed
- Connor McDavid (Edmonton Oilers)
- Sidney Crosby (Pittsburgh Penguins)
- Auston Matthews (Toronto Maple Leafs)

## Questions I Asked
1. Who has the most varied vocabulary?
2. What are each player's signature words?

## What I Found
| Player | Total Words | Unique Words | Richness Score |
|---|---|---|---|
| Sidney Crosby | 957 | 295 | 0.308 |
| Auston Matthews | 1172 | 311 | 0.265 |
| Connor McDavid | ~1100 | ~280 | 0.240 |

- **Crosby** is the most linguistically varied speaker
- **McDavid** is the most repetitive — and says "obviously" as his 
  signature word
- **Matthews** uses hedging language ("think", "mean", "kind") 
  suggesting a more cautious communication style

## What Surprised Me
McDavid is widely considered the best player in the world, yet he has 
the most repetitive interview vocabulary. Crosby, the veteran, 
actually speaks with the most variety.

## How to Run
```bash
python analyzer.py
```

## Libraries Used
- `matplotlib` for bar charts
- Pure Python for all text analysis (dicts, sets, file I/O)