from collections import Counter
t=int(input())
for _ in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    ans=-1
    twos=Counter(arr)
    curr=0
    for i in range(n):
        if arr[i]==2:
            curr+=1
        if curr==twos[2]-curr:
            ans=i+1
            break
    print(ans)
    