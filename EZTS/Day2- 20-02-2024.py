#P1
#Approach - 1
'''
t = int(input())
for i in range(t):
    n = int(input())
    x = int((n*50) - ((0.7)*(n*50)))
    print(x)
'''
#Approach - 2
'''
t = int(input())
while t > 0:
    n = int(input())
    x = int((n*50) - ((0.7)*(n*50)))
    print(x)
    t = t - 1
'''
#Approach - 3
'''
t = int(input())
def test(t):
    if t > 0:
        n = int(input())
        x = int((n*50) - ((0.7)*(n*50)))
        print(x)
    else:
        return
    test(t-1)
test(t)
'''
#Approach - 4
'''
t = int(input())
def profit(n):
    x = int((n*50) - ((0.7)*(n*50)))
    return x
def test(t):
    if t > 0:
        n = int(input())
        print(profit(n))
    else:
        return
    test(t-1)
test(t)
'''
#P2
#Approach - 1
'''
x,y = map(int,input().split())
print((x-y) + (y//2))
'''
#Approach - 2
'''
def movie(x,y):
    print((x-y) + (y//2))
a,b = map(int,input().split())
movie(a,b)
'''
#P3
#Approach - 1
'''
t = int(input())
for i in range(t):
    n = int(input())
    c = 0
    while n > 0:
        if n%10 == 4:
            c = c + 1
        n = n // 10
    print(c)
'''
#Appraoch - 2
'''
def test(n):
    if t == 0:
        return
    else:
        n = int(input())
        print(count(n))
    test(n-1)
def count(n):
    c = 0
    while n > 0:
        r = n%10
        if r == 4:
            c = c + 1
        n = n // 10
    return c
t = int(input())
test(t)
'''
#P4
#Appraoch - 1
'''
n = int(input())
r = 1
for i in range(1,n+1):
    r = r * i
print(r)
'''
#Approach - 2
'''
n = int(input())
r = 1
while n > 0:
    r = r * n
    n = n - 1
print(r)
'''
#Approach - 3
'''
def fact(n):
    if n==0 or n==1:
        return 1
    else:
        return n*fact(n-1)

k=int(input())
print(fact(k))
'''
#P5
'''
n = int(input())
if n%2==0:
    print(n+2)
else:
    print(n+1)
'''
#P6
'''
n=int(input())
def temp(n):
    r=n
    c=0
    while r>0:
        c+=1
        r=r//10
    n=(3*pow(10,c))+n
    n=n*10+3
    return n
print(temp(n))
'''
