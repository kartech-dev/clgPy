

text = "Python is fun and Python is powerful"
words = text.split()
word_count = {}
for word in words:
    word_count[word] = word_count.get(word, 0) + 1  
print(word_count)
