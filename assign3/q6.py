n=int(input('Enter the number:'))
t=n
rev=0
while(n>1):
    dig=n%10
    rev=rev*10+dig
    print(rev)
    n=n//10
    print(n)
if(rev==t):
    print("It is a palindrome")
else:
    print("Not a palindrome")
