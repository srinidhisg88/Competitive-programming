from collections import Counter

t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    freq = Counter(arr)
    
    if len(freq) == 1:
        print("YES")
    elif len(freq) == 2:
        values = list(freq.values())
        # The counts must differ by at most 1 (for alternating pattern)
        if abs(values[0] - values[1]) <= 1:
            print("YES")
        else:
            print("NO")
    else:
        print("NO")