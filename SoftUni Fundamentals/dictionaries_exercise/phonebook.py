given_info = input().split("-")
phonebook = {}

while len(given_info) != 1:
    key = given_info[0]
    value = given_info[1]
    phonebook[key] = value

    given_info = input().split("-")

num = int(given_info[0])
for n in range(num):
    searched_name = input()
    if searched_name in phonebook.keys():
        print(f"{searched_name} -> {phonebook[searched_name]}")
    else:
        print(f"Contact {searched_name} does not exist.")



