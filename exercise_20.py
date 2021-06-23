# Function reads hashtags from hashtags.txt file and writes sorted list of hashtags to a file.
# Length of each hashtag is lower than given length
# (Sign # doesn't count in length of a hashtag)

def clean_hashtags(input_file, output_file, length):
    hashtags = list()
    with open(input_file, 'r', encoding='UTF-8') as file:
        for line in file.readlines():
            hashtags.extend([hashtag.rstrip() for hashtag in line.split(' ')])

    hashtagsWithMaxLengthLetters = sorted(set([hashtag \
                                               for hashtag in hashtags if len(hashtag) <= length + 1]))
    # print(hashtagsWithMaxLengthLetters)

    with open(output_file, 'w', encoding='UTF-8') as file:
        for item in hashtagsWithMaxLengthLetters:
            file.write(item + '\n')


clean_hashtags('TXT_files/hashtags.txt', 'TXT_files/clean5.txt', 5)

