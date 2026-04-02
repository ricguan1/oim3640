import os

def load_text(filename):
    """Read a text file and return its contents as a lowercase string."""
    base_dir = os.path.dirname(os.path.abspath(__file__))
    filepath = os.path.join(base_dir, filename)
    with open(filepath, 'r') as f:
        return f.read().lower()


def get_words(text):
    """Split text into a list of words, removing punctuation."""
    cleaned = ""
    for char in text:
        if char.isalpha() or char == " ":
            cleaned += char
    return cleaned.split()


def count_words(words):
    """Count word frequencies, return a dictionary."""
    counts = {}
    for word in words:
        counts[word] = counts.get(word, 0) + 1
    return counts


def top_n_words(counts, n=10):
    """Return the top n words by frequency as a sorted list of tuples."""
    sorted_words = sorted(counts.items(), key=lambda x: x[1], reverse=True)
    return sorted_words[:n]


def analyze_player(filename, player_name):
    """Run full analysis for one player and print results."""
    text = load_text(filename)
    words = get_words(text)
    counts = count_words(words)
    top = top_n_words(counts)

    print(f"\n=== {player_name} ===")
    print(f"Total words: {len(words)}")
    print(f"Unique words: {len(counts)}")
    print(f"Top 10 words:")
    for word, count in top:
        print(f"  {word}: {count}")


if __name__ == "__main__":
    analyze_player("data/mcdavid.txt", "Connor McDavid")
    analyze_player("data/crosby.txt", "Sidney Crosby")
    analyze_player("data/matthews.txt", "Auston Matthews")