# sa se scrie o Fractie(nuumarator, numitor)care sa implementeze urmatoarele metode:
# __init__ : instantiem numaratorul si numitorul
# __str__ : afisam "numarator/numitor"
# __add__ : returnam o noua fractie care reprezinta adunarea
# __sub__ : returnam o noua fractie care reprezinta scaderea
# inverse: returneaza o noua fractie (inversa fractiei)


# Euclid’s Algorithm states that the greatest common divisor of two integers numerator and denominator is denominator if denominator divides numerator evenly. However, if denominator does not divide numerator evenly, then the answer is the greatest common divisor of denominator and the remainder of nominator divided by denominator.
def euclid_algorithm(numerator, denominator):
    while numerator % denominator != 0:
        old_numerator = numerator
        old_denominator = denominator
        numerator = old_denominator
        denominator = old_numerator % old_denominator
    return denominator


class Fraction:

    @staticmethod
    def inverse(numerator, denominator):
        return Fraction(denominator, numerator)

    def __init__(self, numerator, denominator):
        self.num = numerator
        self.den = denominator

    def __str__(self):
        return str(self.num) + "/" + str(self.den)

    def __add__(self, other_fraction):
        newnum = self.num * other_fraction.den + self.den * other_fraction.num
        newden = self.den * other_fraction.den
        common = euclid_algorithm(newnum, newden)
        return Fraction(newnum // common, newden // common)

    def __sub__(self, other_fraction):
        newnum = self.num * other_fraction.den - self.den * other_fraction.num
        newden = self.den * other_fraction.den
        common = euclid_algorithm(newnum, newden)
        return Fraction(newnum // common, newden // common)


fraction = Fraction('numerator', 'denominator')
print('Example of the fraction itself:', fraction)

first_fraction = Fraction(1, 4)
second_fraction = Fraction(1, 2)
adding_fractions = first_fraction + second_fraction
print('Result of adding fractions:', adding_fractions)

third_fraction = Fraction(3, 9)
forth_fraction = Fraction(1, 7)
deduction_fractions = third_fraction - forth_fraction
print('Result of deducting fraction:', deduction_fractions)

print('Inverse fraction: ', Fraction.inverse(7, 9))

