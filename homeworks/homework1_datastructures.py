numbers_list = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6]

numbers_list.sort()
print(numbers_list)

numbers_list.sort(reverse=True)
print(numbers_list)

numbers_list.sort()
even_number_list = numbers_list[1::2]
print(even_number_list)

uneven_number_list = numbers_list[0::2]
print(uneven_number_list)

multiple_3numbers = numbers_list[2::3]
print(multiple_3numbers)

