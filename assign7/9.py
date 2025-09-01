#Given a list of words, use map() to convert each word to uppercase.
def up(word):
    return word.upper()
words = ["hello", "world", "python", "is", "fun"]
upwords = list(map(up, words))
print(upwords)
