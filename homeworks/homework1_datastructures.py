numbers_list = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6]

numbers_list.sort()
print(numbers_list)

numbers_list.sort(reverse=True)
print(numbers_list)

even_number_list = numbers_list[::2]
even_number_list.sort()
print(even_number_list)

uneven_number_list = numbers_list[1::2]
uneven_number_list.sort()
print(uneven_number_list)

multiple_3numbers = numbers_list[1::3]
multiple_3numbers.sort()
print(multiple_3numbers)