numb = float(input())

if numb == 0:
    print("zero")
elif numb > 0:
    if numb < 1:
        print("small positive")
    elif numb > 1000000:
        print("large positive")
    else:
        print("positive")
else:
    if abs(numb) < 1:
        print("small negative")
    elif abs(numb) > 1000000:
        print("large negative")
    else:
        print("negative")