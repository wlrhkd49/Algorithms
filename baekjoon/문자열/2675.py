for _ in range(int(input())):
    n, s = input().split()
    for i in range(len(s)):
        for _ in range(int(n)):
            print(s[i], end='')
    print()