t=int(input())


for _ in range(t):
    n,k=map(int,input().split())
    boxn=list(map(int,input().split()))
    newarr=sorted(boxn)
    if newarr[:]==boxn[:] or k>1:
        print('YES')
    else:
        print('NO')