list=[1, 2, 3, 2, 4, 2, 5]
j=0
tup1=tuple(list)
for i in range(0,6):
    if tup1[i]==2:
        j=j+1
print(j)