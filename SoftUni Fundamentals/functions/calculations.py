def calculate(command, first_num, second_num):

    result = 0

    if command == "multiply":
        result = first_num * second_num

    elif command == "divide":
        result = int(first_num / second_num)

    elif command == "add":
        result = first_num + second_num

    elif command == "substract":
        result = first_num - second_num

    return result

command = input()
first_num = int(input())
second_num = int(input())

res = calculate(command, first_num, second_num)
print(res)
