# sa se scrie o Fractie(nuumarator, numitor)care sa implementeze urmatoarele metode:
# __init__ : instantiem numaratorul si numitorul
# __str__ : afisam "numarator/numitor"
# __add__ : returnam o noua fractie care reprezinta adunarea
# __sub__ : returnam o noua fractie care reprezinta scaderea
# inverse: returneaza o noua fractie (inversa fractiei)


class Fractie:

    def __init__(self, numarator, numitor):
        self.num = numarator
        self.den = numitor

    def __str__(self):
        return str(self.num) + "/" + str(self.den)

    def __add__(self, otherfraction):
        newnum = self.num * otherfraction.den + self.den * otherfraction.num
        newden = self.den * otherfraction.den
        return Fractie(newnum, newden)

    def __sub__(self, otherfraction):
        newnum = self.num * otherfraction.den - self.den * otherfraction.num
        newden = self.den * otherfraction.den
        return Fractie(newnum, newden)


fraction = Fractie('numarator', 'numitor')
print('Exemplu afisare metoda __str__', fraction)

first_fraction = Fractie(1, 4)
second_fraction = Fractie(1, 2)
adding_fractions = first_fraction + second_fraction
print('Fractia care reprezinta adunarea:', adding_fractions)

third_fraction = Fractie(3, 9)
forth_fraction = Fractie(1, 7)
deduction_fractions = third_fraction - forth_fraction
print('Fractia care reprezinta scaderea:', deduction_fractions)
