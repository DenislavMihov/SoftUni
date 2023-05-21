# occurrences = {}
#
# for letter in input():
#     occurrences[letter] = occurrences.get(letter, 0) +1
#
# for letter, time in sorted(occurrences.items()):
#     print(f"{letter}: {time} time/s")

text = input()

for letter in sorted(set(text)):
    print(f"{letter}: {text.count(letter)} time/s")