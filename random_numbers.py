import random
import secrets
import numpy as np
a = random.uniform(1,16)
print(a)
b=random.rang(1,17)
print(b)
contest_winner=random.normalvariate(0,10000)
print(contest_winner)
numbers=list(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17)
print(numbers)
t=random.choice(numbers)
print(t)
random.shuffle(numbers)
random.seed(1)
print(random.random())
print(random.randint(1,10))
random.seed(2)
print(random.random())
print(random.randint(1,10))
a = secrets.randbelow(10)
print(a)
k=secrets.randbits(8)
print(k)
mylist=list("ABCDEFGHIJKLMNOPQRS")
s = secrets.choice(mylist)
print(s)
a = np.random.randint(1,15,(3,4))
print(a)
arr = np.array([1,2,3], [4,5,6])
print(arr)
np.random.shuffle(arr)
print(arr)
