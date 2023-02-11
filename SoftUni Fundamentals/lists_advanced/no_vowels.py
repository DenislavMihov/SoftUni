text = input()
forbidden_letters = ['a', 'o', 'u', 'e', 'i']
result = [char for char in text if char.lower() not in forbidden_letters]


#for char in text:
#    # make case insensitive
#    if char.lower() not in forbidden_letters:
#       result.append(char)

print("".join(result))