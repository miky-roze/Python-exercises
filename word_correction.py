# Create a function that take a word as argument
# and returns 5 other words that are the closest (in terms of levenshtein distance) to the given word.
# Words are chosen form an exemplary bank of words.

from levenshtein_distance import lev


def get_similar(word):

    exemplaryBankWord = [
        'friend',
        'friends',
        'friendship',
        'fry',
        'data',
        'database',
        'data science',
        'big data',
        'data cleaning',
        'date'
    ]

    levDistance = list()
    for exemplaryWord in exemplaryBankWord:
        levDistance.append((exemplaryWord, lev(word, exemplaryWord)))

    levDistance = sorted(levDistance, key=lambda item: item[1])

    return levDistance[:5]
