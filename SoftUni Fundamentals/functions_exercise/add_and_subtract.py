def sum_numbers(first_num, second_num):
    result = first_num + second_num
    return  result

first_number = int(input())
second_number = int(input())
first_result = sum_numbers(first_number, second_number)

def subtract(first_num, second_num):
    result = first_num - second_num
    return result

first_number = first_result
third_number = int(input())
final_result = subtract(first_number, third_number)
print(final_result)