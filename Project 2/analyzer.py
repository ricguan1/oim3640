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
    "what", "know", "yeah", "uh", "um", "minutes", "secondsyeah", "im", 
    "hes", "its", "when", "not", "very","going", "here", "there", "can", 
    "right", "got", "as", "much", "little", "thats", "theres", "from", "no", 
    "about", "always", "want", "think", "into", "really", "bit", "guys", 
    "secondsi", "secondsyou", "secondsand", "youre", "ive", "minute"
    "minute", "secondsand", "youre", "ive", "all", "how", "oh", "still", "who"
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

import matplotlib.pyplot as plt

def plot_top_words(all_player_data):
    """Create a bar chart comparing top 5 words for each player."""
    fig, axes = plt.subplots(1, len(all_player_data), figsize=(15, 5))
    fig.suptitle("Top 5 Most Common Words by NHL Player", fontsize=14)

    for ax, (name, counts) in zip(axes, all_player_data):
        top = top_n_words(counts, 5)
        words = [w for w, c in top]
        freqs = [c for w, c in top]
        ax.bar(words, freqs, color='steelblue')
        ax.set_title(name)
        ax.set_ylabel("Frequency")
        ax.set_xlabel("Word")

    plt.tight_layout()
    plt.savefig("word_chart.png")
    print("\nChart saved as word_chart.png")

def compare_players(players):
    """Print a ranked comparison of all players by vocabulary richness."""
    print("\n" + "="*40)
    print("VOCABULARY RICHNESS RANKING")
    print("="*40)
    ranked = sorted(players, key=lambda x: x[1], reverse=True)
    for i, (name, score) in enumerate(ranked, 1):
        print(f"  {i}. {name}: {score}")
        
if __name__ == "__main__":
    results = []
    chart_data = []

    for filename, name in [("data/mcdavid.txt", "Connor McDavid"),
                            ("data/crosby.txt", "Sidney Crosby"),
                            ("data/matthews.txt", "Auston Matthews")]:
        text = load_text(filename)
        words = get_words(text)
        clean = remove_stop_words(words)
        counts = count_words(clean)
        richness = vocab_richness(counts, len(words))
        results.append((name, richness))
        chart_data.append((name, counts))
        analyze_player(filename, name)

    compare_players(results)
    plot_top_words(chart_data)