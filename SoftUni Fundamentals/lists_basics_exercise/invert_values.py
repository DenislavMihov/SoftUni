#list_of_numbers = input().split()
#opposite_numbers = []
#for element in list_of_numbers:
#    opposite_numbers.append((-int(element))

#print(opposite_numbers)



numbers_in_strings = input()

my_list_in_strings = numbers_in_strings.split()

my_list = [int(x) for x in my_list_in_strings]

invert_values = []

for n in my_list:
    if n > 0:
        invert_num = n * (-1)
        invert_values.append(invert_num)

    elif n < 0:
        invert_num = n * (-1)
        invert_values.append(invert_num)

    else:
        invert_values.append(n)

print(invert_values)

