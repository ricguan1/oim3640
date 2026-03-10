def uses_only(word, letters):
    """does word use only the allowed letters?"""
    for letter in word:
        if letter not in letters:
            return False
    return True

def is_valid(word, letters, required):
    """is word valid"""
    return uses_only(word, letters) and must_use(word, required) and len(word) >= 4

def find_words(letters, required):
    """find all words that are valid"""
    with open ('words.txt') as word_file:
        for word in word_file:
            word = word.strip()
            if is_valid(word, letters, required):
                print(word)


print(uses_only('cake', 'kcboela'))
print(uses_only('babson', 'kcboela'))
print(uses_only('tacoma', 'kcboela'))
print(uses_only('python', 'kcboela'))
valid_words = find_words ('kcboela', 'a')
print(valid_words)

if__name_ == '__main__'
main()