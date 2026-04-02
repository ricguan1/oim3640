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

STOP_WORDS = {
    "the", "a", "an", "and", "or", "but", "in", "on", "at", "to",
    "for", "of", "with", "i", "you", "he", "she", "it", "we", "they",
    "is", "was", "are", "were", "be", "been", "have", "has", "had",
    "do", "did", "that", "this", "my", "your", "his", "her", "our",
    "me", "him", "us", "them", "so", "just", "like", "up", "out",
    "what", "know", "yeah", "uh", "um", "minutes"
}

def remove_stop_words(words):
    """Filter out common stop words and filler words."""
    return [word for word in words if word not in STOP_WORDS]

def vocab_richness(counts, total_words):
    """Return ratio of unique words to total words (0-1 scale)."""
    return round(len(counts) / total_words, 3)

def top_n_words(counts, n=10):
    """Return the top n words by frequency as a sorted list of tuples."""
    sorted_words = sorted(counts.items(), key=lambda x: x[1], reverse=True)
    return sorted_words[:n]


def analyze_player(filename, player_name):
    text = load_text(filename)
    words = get_words(text)
    clean = remove_stop_words(words)
    counts = count_words(clean)
    top = top_n_words(counts)
    richness = vocab_richness(counts, len(words))

    print(f"\n=== {player_name} ===")
    print(f"Total words: {len(words)}")
    print(f"Unique words (after cleaning): {len(counts)}")
    print(f"Vocabulary richness score: {richness}")
    print(f"Top 10 meaningful words:")
    for word, count in top:
        print(f"  {word}: {count}")


if __name__ == "__main__":
    analyze_player("data/mcdavid.txt", "Connor McDavid")
    analyze_player("data/crosby.txt", "Sidney Crosby")
    analyze_player("data/matthews.txt", "Auston Matthews")