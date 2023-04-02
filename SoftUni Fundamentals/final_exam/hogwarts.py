string = input()
data = input()
while data != "Abracadabra":
    command = data.split()

    if command[0] == "Abjuration":
        string = string.upper()
        print(string)

    elif command[0] == "Necromancy":
        string = string.lower()
        print(string)


    elif command[0] == "Illusion":

        index = int(command[1])

        letter = command[2]

        if index < 0 or index >= len(string):

            print("The spell was too weak.")

        else:

            string = string[:index] + letter + string[index + 1:]

            print("Done!")

    elif command[0] == "Divination":
        first_substring = command[1]
        second_substring = command[2]

        if first_substring in string:
            string = string.replace(first_substring, second_substring)

            print(string)
        else:
            continue


    elif command[0] == "Alteration":
        substring = command[1]

        if substring in string:
            string = string.replace(substring, "")
            print(string)

        else:
            print("The spell was too weak.")

    else:
        print("The spell did not work!")

    data = input()