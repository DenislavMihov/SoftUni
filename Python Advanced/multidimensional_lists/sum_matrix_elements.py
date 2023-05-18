rows, cols = [int(x) for x in input().split(", ")]

matrix = []
sum = 0

for _ in range(rows):
    inner_list = []
    numbers_as_strings = input().split(", ")
    for num in numbers_as_strings:
        inner_list.append(int(num))

    #inner_list = [int(el) for el in input().split(", ")

    matrix.append(inner_list)

for row_index in range(rows):
    for col_index in range (cols):
        sum += matrix[row_index][col_index]

print(sum)
print(matrix)

