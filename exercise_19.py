# Function reads hashtags from hashtags.txt file and returns sorted list of hashtags which length is lower than 4
# (Sign # doesn't count in length of a hashtag)

def clean_hashtags():
    hashtags = list()
    with open('TXT_files/hashtags.txt', 'r', encoding='UTF-8') as file:
        for line in file.readlines():
            hashtags.extend([hashtag.rstrip() for hashtag in line.split(' ')])

    hashtagsWithMax4Letters = [hashtag for hashtag in hashtags if len(hashtag) <= 5]
    hashtagsWithMax4Letters.append('#ufc')

    return sorted((set(hashtagsWithMax4Letters)))


print(clean_hashtags())
