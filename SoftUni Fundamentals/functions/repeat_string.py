string = input()
n = int(input())

repeat_string = lambda a, b: a * b
res = repeat_string(string, n)
print(res)