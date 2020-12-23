class Checker:

    def __init__(self, three_numbers_l):
        self.three_numbers_l = three_numbers_l

    def check(self, x):
        if sum(self.three_numbers_l) == x:
            print('Сумма трех чисел равна x')
        else:
            print('Сумма трех чисел не равна x')


my_checker = Checker([1, 2, 3])

my_checker.check(7)
