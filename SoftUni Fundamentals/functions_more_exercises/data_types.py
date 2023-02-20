def data_types(arg1, arg2):
    if arg1 == "int":
       result = int(arg2) * 2
       return result
    elif arg1 == "real":
        result = float(arg2) * 1.5
        return f"{result:.2f}"
    elif arg1 == "string":
        result = str(arg2)
        return f"${result}$"


command = input()
number = input()

print(data_types(command, number))