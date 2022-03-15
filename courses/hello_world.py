# print("Hello, world!")
# print("second")
# print("3 8")

# print(type(3)), float(3), type(float(3)), complex(3), type(complex(3))
# print(type(2.5)), int(2,5), type(int(2,5)), type(complex(2,5))
# print(type(3+2j))

# print(10 % 2)
# print(1 in [1,2,3])
# print("a" in "python")

# my_variable = 3
# print(my_variable, type(my_variable), id(my_variable))
# my_variable = 4.5
# print(my_variable, type(my_variable))
# my_variable = True
# print(my_variable, type(my_variable), id(my_variable))
# my_variable = None
# print(my_variable, type(my_variable), id(my_variable))

# a = 300
# b = 7
# print(a == b, a is b)

# show all defined variables from built-in namespace
# print(dir(__builtins__))

# my_string = "print(22)"
# print(my_string, "my_string")

# modalitati de a formata stringurile:
# A
price = 2
address = 'Carol 1'
city = 'Bucuresti'
# my_string = 'am cumparat o gogoasa cu ' + str(price) + ' lei' #concatenare
# my_string = 'am cumparat o gogoasa cu {} lei, de la magazinul din stada {}, {}'.format(price, address, city) # {}= place holdere, in parantezele de la format sunt parametrii si se afla pe pozitii incepand cu 0, 1, 2
my_string = 'am cumparat o gogoasa cu {2} lei, de la magazinul din stada {0}, {1}'.format(address, city, price)
print(my_string)

# B
price = 22.50
address = 'Carol 1'
city = 'Bucuresti'
my_string = 'am cumparat o gogoasa cu %.2f lei, de la magazinul din stada %s, %s' % #.2f inseamna 2 decimale pt un float
print(my_string)

# C - f string
price = 22.50
address = 'Carol 1'
city = 'Bucuresti'
my_string = f'am cumparat o gogoasa cu{price} lei, de la magazinul din stada {address}, {city}'
print(my_string)