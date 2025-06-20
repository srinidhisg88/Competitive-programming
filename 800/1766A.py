
# pre computation
def check(x):
    count_zeros=0
    count_digits=0
    while x:
        sub=x%10
        if sub==0:
            count_zeros+=1
        count_digits+=1
        x=x//10
    return count_zeros==count_digits-1


arr=[]
for i in range(1,1000000):
    if check(i):
        arr.append(i)

t=int(input())
for _ in range(t):
    ans=0
    n=int(input())
    for i in range(len(arr)):
        if arr[i]<=n:
            ans+=1
        else:
            break
    print(ans)
