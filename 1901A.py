t=int(input())
for _ in range(t):

    n,x=map(int,input().split())
    points=list(map(int,input().split()))
    max_dist=float('-inf')
    for i in range(1,n):
        max_dist=max(max_dist,points[i]-points[i-1])
    max_dist=max(max_dist,points[0])
    max_dist=max(max_dist,2*(x-points[-1]))
    print(max_dist)
