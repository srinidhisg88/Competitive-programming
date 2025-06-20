t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    max_val = max(a)

    group_a = [x for x in a if x != max_val]
    group_b = [x for x in a if x == max_val]

    if not group_a:
        print(-1)
    else:
        print(len(group_a), len(group_b))
        print(*group_a)
        print(*group_b)