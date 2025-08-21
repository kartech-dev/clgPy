import random
random_unique_numbers = random.sample(range(1, 100), 4)
n=int(input("Enter your guess!!!" \
" "))
print(random_unique_numbers)
if n in random_unique_numbers :
    print("Found")
else:
    print("Not Found")
