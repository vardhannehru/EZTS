#P1
#Appraoch - 1
'''
n = int(input())
a = list(map(int,input().split()))[:n]
for i in range(n):
    if a[i] in a[i+1:]:
        print(a[i])
        break
'''
#Approach - 2
'''
n = int(input())
a = list(map(int,input().split()))[:n]
a.sort()
for i in range(n-1):
    if a[i]==a[i+1]:
        print(a[i])
        break
'''
#Approach - 3
'''
n = int(input())
a = list(map(int,input().split()))[:n]
for i in a:
    c = a.count(i)
    if c > 1:
        print(i)
        break
'''
#P3
#Approach - 1
'''
n=int(input())
l=list(map(int,input().split()))[:n]
unique=[]
for i in range(n):
    if l.count(l[i])==1:
        if l[i] in unique:
            continue
        else:
            unique.append(l[i])

for i in unique:
    print(i,end=" ")
'''
#Approach - 2
'''
n = int(input())
a = list(map(int,input().split()))[:n]
for i in a:
    if a.count(i) == 1:
        print(i,end=" ")
'''
#P4
#Approach - 1
'''
t = int(input())
for i in range(t):
    n = int(input())
    t1 = 0
    t2 = 0
    for j in range(1,n+1):
        if n%j == 0:
            if j%2 == 0:
                t1 = t1 + 1
            else:
                t2 = t2 + 1
    if t1 == t2:
        print(1)
    else:
        print(0)
'''
#Appraoch - 2
'''
t = int(input())
for i in range(t):
    n = int(input())
    factors = []
    for j in range(1,n+1):
        if n%j == 0:
            factors.append(j)
    ef = []
    of = []
    for j in factors:
        if j%2==0:
            ef.append(j)
        else:
            of.append(j)
    if len(ef)==len(of):
        print(1)
    else:
        print(0)
'''
#P5
#Approach - 1
'''
t = int(input())
for i in range(t):
    n,x = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    c = 0
    for j in range(n):
        if a[j] >= x:
            c = c + b[j]
    print(c)
'''
#P6 (Prime / Not)
#Approach - 1
'''
n = int(input())
for i in range(2,n+1):
    if n%i==0:
        print("Not a Prime")
else:
    print("Prime")
'''
#Approach - 2
'''
n = int(input())
fc = []
for i in range(1,n+1):
    if n%i == 0:
        fc.append(i)
if len(fc) == 2:
    print('Prime')
else:
    print("Not a Prime")
'''
#P7
'''
t = int(input())
for ii in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    happy = 0
    for i in range(n):
        if a[i] <= 2*bob[i] and b[i]<=2*a[i]:
            happy += 1
    print(happy)
'''
#P8(Print all the even perfect numbers in a given range)
#Approach - 1
'''
n=int(input())
for i in range(1,n+1):
    factors=[]
    if i%2==0:
        for j in range(1,i):
            if i%j==0:
                factors.append(j)
        if sum(factors)==i:
            print(i)
'''
#Approach - 2
'''
n=int(input())
s=0
for i in range(2,n+1,2):
    for j in range(1,i):
        if i%j==0:
            s+=j
    if s==i:
        print(i)
    s=0
'''
