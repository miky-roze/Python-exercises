# Create a function that calculates Levenshtein distance between two finite words.
# More on Levenshtein distance: https://en.wikipedia.org/wiki/Levenshtein_distance

def lev(word, otherWord):
    if not isinstance(word, str):
        raise TypeError(f"Word must be of type 'str'. NOT {type(word)}")
    if not isinstance(otherWord, str):
        raise TypeError(f"Other word must be of type 'str'. NOT {type(otherWord)}")

    if len(word) == 0:
        return len(otherWord)
    elif len(otherWord) == 0:
        return len(word)
    elif word[0] == otherWord[0]:
        return lev(word[1:], otherWord[1:])
    else:
        return 1 + min(lev(word[1:], otherWord), lev(word, otherWord[1:]), lev(word[1:], otherWord[1:]))
