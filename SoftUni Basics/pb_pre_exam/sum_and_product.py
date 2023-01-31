n = int(input())



for a in range(1, 9 + 1):
    for b in range(9, a +1):
        for c in range(0, 9 + 1):
            for d in range(9, c + 1):
                print(a,b,c,d)
