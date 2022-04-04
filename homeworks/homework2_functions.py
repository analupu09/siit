# o functie care primeste un numar nedefinit de parametri si sa se calculeze suma parametrilor care reprezinta numere intregi sau reale
# your_function(1, 5, -3, 'abc', [12, 56, 'cad']) va returna 3 (1+5-3)
# your_function() va returna 0
# your_function(2, 4, 'abc', param_1=2) va returna 6(2+4)


def undefined_params(*args, **kwargs):
    a = 0

    for x in args + tuple(kwargs.values()):
        try:
            nr = int(x)
            a += x
        except:
            try:
                nr = float(x)
                a += nr
            except:
                pass

    return a

print( f'Beginning of exercise 1.\n','case_1 = ',undefined_params(1, 5, -3, 'abc', [12, 56, 'cad']))
print(f'case_2 = ',undefined_params())
print('case_3 = ',undefined_params(2, 4, 'abc', param_1=2), f'\nEnd of exercise 1.')



# o functie recursiva care primeste ca parametru un numar intreg si returneaza:
# suma tuturor numerelor de la [0,n]
# suma numerelor pare de la [0, n]
# suma numerelor impare de la [0,n]

n = 9
def multiple_reccursive_values(n):
    if n == 0:
        return 0, 0, 0

    old_total, old_even, old_odd = multiple_reccursive_values(n-1)
    total = n + old_total
    if n % 2 == 0:
        even = old_even + n
        odd = old_odd
    else:
        even = old_even
        odd = old_odd + n

    return total, even, odd


sum_total_numbers, sum_even_numbers, sum_odd_numbers = multiple_reccursive_values(n)
print('\nBeginning of exercise 2. \ntotal_no = ', sum_total_numbers)
print('even_no = ', sum_even_numbers)
print('odd_no = ', sum_odd_numbers)
print('End of exercise no.2.\n')


# o functie care citeste de la tastatura si returneaza valoarea daca aceasta este un numar intreg, altfel returneaza valoarea 0.

def function_user_input(user_input):
    try:
        if int(user_input):
            print(f'You wrote the following number, which is an int: {user_input}', '\nEnd of exercise')
    except ValueError:
        print(f'This is not an int, therefore its value is: {"0"}', '\nEnd of exercise.')



user_input = input('This is the beginning of the third exercise\nWrite a number or a word: ')
function_user_input(user_input)
