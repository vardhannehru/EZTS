Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#P1
'''
a = int(input())
b = int(input())
if a > b:
    print(a)
else:
    print(b)
'''
#P2
... '''
... a = int(input())
... b = int(input())
... c = int(input())
... if a>b and a>c:
...     print(a)
... elif b>c:
...     print(b)
... else:
...     print(c)
... '''
... #P3
... '''
... a = int(input())
... b = int(input())
... if a > b:
...     print(b)
... else:
...     print(a)
... '''
... #P4
... '''
... a = int(input())
... b = int(input())
... c = int(input())
... if a>b and a>c:
...     a=0
... elif b>c:
...     b=0
... else:
...     c=0
... if a>b and a>c:
...     print(a)
... elif b>c:
...     print(b)
... else:
...     print(c)
... '''
... #P5
... '''
... for i in range(1000):
...     print("Hello World")
... '''
... #P6
... '''
... a,b = map(int,input().split())
... if a==b:
    print("a == b")
elif a>b:
    print("a > b")
else:
    print("a < b")
'''
#P7
#Approach - 1
'''
n = int(input())
if n > 0:
    res=0
    while n > 0:
        r = n%10
        res = (res*10)+r
        n = n//10
    print(res)
elif n == 0:
    print(n)
else:
    res=0
    n=n*-1
    while n > 0:
        r = n%10
        res = (res*10)+r
        n = n//10
    print(-1*res)
'''
#P8
#Approach - 1
'''
w = int(input())
if w>2 and w%2==0:
    print("Yes")
else:
    print("No")
'''
#Approach - 2
'''
w = int(input())
if w%2==0:
    if w > 2:
        print("Yes")
    else:
        print("No")
else:
    print("No")
'''
#P9
#Appraoch - 1
'''
t = int(input())
for i in range(t):
    n = int(input())
    if n > 98:
        print("Yes")
    else:
        print("No")
'''
#Approach - 2
'''
t = int(input())
while t > 0:
    n = int(input())
    if n > 98:
        print("Yes")
    else:
        print("No")
    t = t - 1
'''
#P10
'''
t = int(input())
for i in range(t):
    n = int(input())
    print(100-n)
'''
#P11
'''
t = int(input())
for i in range(t):
    a,b,c,d = map(int,input().split())
    if a-c > b-d:
        print("Second")
    elif a-c < b-d:
        print("First")
    else:
        print("Any")
'''
#P12
'''
t = int(input())
for i in range(t):
    n,x = map(int,input().split())
    if n > x:
        k = n - x
        if k%4==0:
            print(k//4)
        else:
            print((k//4)+1)
    else:
        print(0)
'''
#P13
'''
t = int(input())
for i in range(t):
    n,x = map(int,input().split())
    ts = n * x
    tp = 0
    while ts >= 4:
        tp = tp + 1
        ts = ts - 4
    if ts == 0:
        print(tp)
    else:
        print(tp+1)
'''
#Approach - 2
'''
t = int(input())
for i in range(t):
    n,x = map(int,input().split())
    k = n*x
    if k%4 == 0:
        print(k//4)
    else:
        print((k//4)+1)
'''
