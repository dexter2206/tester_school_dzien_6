text = 'Ala ma kota!'
hist = {'a': 4, 'm': 1, 'k': 1, 'l': 1, 'o': 1, 't': 1, 'others': 3}

def histogram(text):
    """Calculate frequency table of characters in text."""
    hist = {}

    for char in text.lower():
        if char.isalpha():
            hist[char] = hist.get(char, 0) + 1
        else:
            hist['others'] = hist.get('others', 0) + 1
    return hist

print(histogram('Ala ma Kota!'))