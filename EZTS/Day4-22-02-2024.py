#P1
#Approach - 1
'''
s = input()
s1 = set(s)
if len(s1) == 27:
    print("Pangram")
else:
    print("Not a Pangram")
'''
#Approach - 2
'''
alpha = {'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'}
s = input()
d={}
for i in s:
    if i in alpha:
        if i not in d:
            d[i] = 1
        else:
            d[i]+= 1
x = d.keys()
print(d)
if len(x) == 26:
    print("Pangram")
else:
    print("Not a Pangram")
'''
#P2
#Appraoch - 1
'''
t = int(input())
for i in range(t):
    s = input()
    d = {}
    for i in s:
        if i in d:
            d[i] = d[i] + 1
        else:
            d[i] = 1
    for i in d:
        if d[i] == 2:
            print(i)
            break
    else:
        print(".")
'''
#P3
'''
#Approach - 1
n = int(input())
d = {}
for i in range(n):
    name,num = input().split()
    d[name] = num
while True:
    s = input()
    if s in d:
        print(f"{s}={d[s]}")
    else:
        print("Not Found")
'''
#P4
'''
n = int(input())
d = {}
for i in range(n):
    s = input()
    if s in d:
        d[s] = d[s]+1
    else:
        d[s] = 1
#print(d)
x = max(d.values())
z = []
for i in d:
    if d[i] == x:
        z.append(i)
print(max(z),x)
'''
#P5
'''
t = int(input())
for i in range(t):
    n,r = map(int,input().split())
    d = {}
    for j in range(r):
        sid,cid = map(int,input().split())
        if cid not in d:
            d[cid] = [sid]
        else:
            d[cid].append(sid)
    print(d)
    for j in d:
        if len(d[j]) > n and len(set(d[j])==len(d[j]):
            print(f"Scenario #{i+1} : Impossible")
            break
    else:
        print(f"Scenario #{i+1} : Possible")
'''
#P7
'''
n = int(input())
route = {}
for i in range(n):
    c1,c2 = input().split()
    if c1 not in route:
        route[c1] = [c2]
    else:
        route[c1].append(c2)
print(route)
city = input()
if city in route:
    print(*route[city],sep=" ")
else:
    print("None")
'''