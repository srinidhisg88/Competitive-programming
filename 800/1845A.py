t = int(input())
for _ in range(t):
    n, k, x = map(int, input().split())
    if x != 1:
        print("YES")
        print(n)
        print(*[1 for _ in range(n)])
    else:
        if k == 1 or (k == 2 and n % 2 == 1):
            print("NO")
        else:
            print("YES")
            if n % 2 == 0:
                print(n // 2)
                print(*[2 for _ in range(n // 2)])
            else:
                print((n - 3) // 2 + 1)
                print(*([2 for _ in range((n - 3) // 2)] + [3]))