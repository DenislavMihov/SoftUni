word = input()

res = [idx for idx in range(len(word)) if word[idx].isupper()]

print(res)