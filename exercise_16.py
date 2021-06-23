# Function hamming_distance calculates the hamming distance between two vectors
# Function hamming_weight calculates the hamming weight of a vector

def hamming_distance(v1, v2):
    if not len(v1) == len(v2):
        raise ValueError('Both vectors must be the same length.')

    hammingDistance = 0

    for value1, value2 in zip(v1, v2):
        if not value1 == value2:
            hammingDistance += 1

    return hammingDistance


def hamming_weight(vector):
    return vector.count('1')


print(hamming_distance('10111011', '10101011'))
print(hamming_weight('10111011'))
