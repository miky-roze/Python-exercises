# Function slices the given word on strings of given length
# Example: word='python', length=3 ---> [pyt, yth, tho, hon]

def get_slices(word, lenOfSlices):
    if lenOfSlices < 1:
        raise ValueError('The length cannot be less than 1.')
    elif lenOfSlices > len(word):
        raise ValueError('The length cannot be greater than sequence.')

    slices = list()
    end = lenOfSlices
    start = 0
    while end <= len(word):
        slices.append(word[start:end])
        start += 1
        end += 1

    return slices


print(get_slices('python', 3))
