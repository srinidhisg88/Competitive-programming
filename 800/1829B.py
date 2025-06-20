t=int(input())
for _ in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    maxlen=float('-inf')
    cnt=0
    for a in arr:
        if a==0:
            cnt+=1
        else:
            cnt=0
        maxlen=max(maxlen,cnt)
    print(maxlen)