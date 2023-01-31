number = int(input())
start = 97


for first in range(start,start +number):
    for second in range(start,start +number):
        for third in range(start,start +number):
            print(chr(first), chr(second), chr(third), sep="")
