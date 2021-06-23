# Function calculates the score of a given word (like in the Scrabble game)
# Punctation:
# empty (represented by space) - 0 pkt
# EAIONRSTUL - 1 pts
# DG - 2 pts
# BCMP - 3 pts
# FHVWY - 4 pts
# K - 5 pts
# JX - 8 pts
# ZQ - 10 pts

def score(word):
    punctation = {' ': 0, 'EAIONRSTUL': 1, 'DG': 2, 'BCMP': 3, 'FHVWY': 4, 'K': 5, 'JX': 8, 'ZQ': 10}

    score = 0

    for char in word:
        for key in punctation.keys():
            if char.upper() in key:
                score += punctation[key]
                break

    return score


print(score('You are awesome. Thank you for reviewing my code!'))
