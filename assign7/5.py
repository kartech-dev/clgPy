def is_palindrome(word):
    return word == "".join(reversed(word))
print(is_palindrome("radar"))
print(is_palindrome("hello"))
print(is_palindrome("level"))
print(is_palindrome("malayalam"))