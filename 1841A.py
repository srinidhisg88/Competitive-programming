from math import ceil

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    x = input()
    s = input()

    ans=-1
    x0=x
    x1=x0+x0
    x2=x1+x1
    x3=x2+x2
    x4=x3+x3
    x5=x4+x4
    if s in x0:
        ans=0
    elif s in x1:
        ans=1
    elif s in x2:
        ans=2
    elif s in x3:
        ans=3
    elif s in x4:
        ans=4
    elif s in x5:
        ans=5
    print(ans)