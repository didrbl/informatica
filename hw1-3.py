class Checker:

    check_res: float

    def __init__(self, three_numbers_l):
        self.three_numbers_l = three_numbers_l

    def check(self, x):
        self.check_res = sum(self.three_numbers_l) == x
        if self.check_res:
            print('Сумма трех чисел равна x')
        else:
            print('Сумма трех чисел не равна x')


a, b, c = 60, 50, 70 # вводим значение углов треугольника

three_numbers_l = [a, b, c] # вводим значение углов треугольника

my_checker = Checker(three_numbers_l)

my_checker.check(180)
#
# # выводим ответ
if (a > 0 and b > 0 and c > 0) and (a < 180 and b < 180 and c < 180) and my_checker.check_res:
    print("a, b, c могут быть углами треугольника")
else:
    print("a, b, c не могут быть углами треугольника")
