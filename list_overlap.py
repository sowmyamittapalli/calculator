#a = [1, 1, 2, 3, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
import random
a = []
b = []
a = random.sample(xrange(100),20)
print(a)
b = random.sample(xrange(100),10)
print(b)
c = []
for i in a:
    for j in b:
        if(i == j) and (i not in c):
            c.append(i)
print(c)

