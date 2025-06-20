n=int(input())
arr=list(map(int,input().split()))
if 0 in arr:
    print(0)
else:
    min_val=float('inf')
    for i in range(n):
        if abs(arr[i])<min_val:
            min_val=abs(arr[i])
    print(min_val)


