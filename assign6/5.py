#Write a program to store details of a book (title, author, price). Iterate through the dictionary and print each key and value.
book = {
    "title": "The Great Gatsby",
    "author": "F. Scott Fitzgerald",
    "price": 10.99
}
for key, value in book.items():
    print(f"{key}: {value}")
        