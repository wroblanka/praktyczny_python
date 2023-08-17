import glob

POS_SOURCE_FILES = glob.glob('M03/data/aclImdb/train/pos/*.txt')
NEG_SOURCE_FILES = glob.glob('M03/data/aclImdb/train/neg/*.txt')
CHARACTERS_TO_REPLACE = (".",",","!","?")   # "<br />")
HTML_symbol = ("<br />")
pos_reviews = []
neg_reviews = []

for file_name in POS_SOURCE_FILES:
    reviews = []
    with open(file_name, encoding='utf-8') as stream:
        content = stream.read()
        content = content.replace(HTML_symbol,' ')
        content = content.split(' ')
        reviews.append(content)
        for words in reviews:
            for characters in CHARACTERS_TO_REPLACE:
                for word in words:
                    word = word.replace(characters,' ')
            pos_reviews.append(words)

print(pos_reviews[1-6])

for file_name in NEG_SOURCE_FILES:
    reviews = []
    with open(file_name, encoding='utf-8') as stream:
        content = stream.read()
        content = content.replace(HTML_symbol,' ')
        content = content.split(' ')
        reviews.append(content)
        for words in reviews:
            for characters in CHARACTERS_TO_REPLACE:
                for word in words:
                    word = word.replace(characters,' ')
            neg_reviews.append(words)

user_comment = input("Please enter a comment to analyze: ")
user_words = user_comment.lower().split()

sentiment_sum = 0
word_count = len(user_words)

for user_word in user_words:
    positive_counts = 0
    negative_counts = 0
    for review in pos_reviews:
        if user_word in review:
            positive_counts += 1
    for review in neg_reviews:
        if user_word in review:
            negative_counts += 1
    sentiment_word = ((positive_counts - negative_counts) / (positive_counts + negative_counts))
    sentiment_sum += sentiment_word
    print(user_word, sentiment_word)
    
sentiment_avg = sentiment_sum / word_count

if sentiment_avg >= 0:
    print("The comment is positive.", "sentiment =", sentiment_avg)
else:
    print("The comment is negative.", "sentiment =", sentiment_avg)