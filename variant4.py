def main():
    fl = True
    while fl:
        x = input("Введите действительную часть первого комплексного числа: ")
        while not in_float(x):
            print("Введено неверное значение! Ожидалось вещественное или целое число.")
            x = input("Введите действительную часть первого комплексного числа: ")
            in_float(x)
        x = float(x)
        y = input("Введите мнимую часть первого комплексного числа: ")
        while not in_float(y):
            print("Введено неверное значение! Ожидалось вещественное или целое число.")
            y = input("Введите мнимую часть первого комплексного числа: ")
            in_float(y)
        y = float(y)
        z = input("Введите действительную часть второго комплексного числа: ")
        while not in_float(z):
            print("Введено неверное значение! Ожидалось вещественное или целое число.")
            z = input("Введите действительную часть второго комплексного числа: ")
            in_float(z)
        z = float(z)
        u = input("Введите мнимую часть второго комплексного числа: ")
        while not in_float(u):
            print("Введено неверное значение! Ожидалось вещественное или целое число.")
            u = input("Введите действительную часть второго комплексного числа: ")
            in_float(u)
        u = float(u)
        n = input("Введите n: ")
        while not in_int(n):
            print("Введено неверное значение! Ожидалось целое число.")
            n = input("Введите n: ")
            in_int(n)
        n = int(n)
        num1 = complex(x, y)
        num2 = complex(z, u)
        print("Число 1:", num1)
        print("Число 2:", num2)
        choice(x, num1, num2, n)
        flag = True
        while flag:
            examples_1()
            choice_1 = input("Выбор(1 - 3): ")
            while choice_1 != "1" and choice_1 != "2" and choice_1 != "3":
                print("Введено неверное значение! Ожидалось 1, 2 или 3.")
                examples_1()
                choice_1 = input("Выбор(1 - 3): ")
            choice_1 = int(choice_1)
            if choice_1 == 1:
                choice(x, num1, num2, n)
            if choice_1 == 2:
                flag = False
            if choice_1 == 3:
                flag = False
                fl = False


def in_float(num):
    try:
        float(num)
        return True
    except ValueError:
        return False


def in_int(num):
    try:
        int(num)
        return True
    except ValueError:
        return False


def examples():
    print("1. Сумма       3. Произведение       5. Возведение в степень")
    print("2. Разность    4. Сравнение числе    6. Корень в степени n из числа")


def examples_1():
    print("1. Продолжить вычисления\n2. Изменить числа\n3. Выход")


def choice(x1, x, y, degree):
    examples()
    n = input("Какое действие вы хотите выполнить с этими числами(1 - 6)? ")
    while n != "1" and n != "2" and n != "3" and n != "4" and n != "5" and n != "6":
        print("Введено неверное значение! Ожидалось 1, 2, 3, 4, 5 или 6.")
        examples()
        n = input("Какое действие вы хотите выполнить с этими числами(1 - 6)? ")
    n = int(n)
    if n == 1:
        summa_complex(x, y)
    elif n == 2:
        dif_complex(x, y)
    elif n == 3:
        multiplication_complex(x, y)
    elif n == 4:
        check_num(x, y)
    elif n == 5:
        exponentiation_complex_num1(x, degree)
    elif n == 6:
        if x1 < 0:
            print("Корень вычислить невозможно, так как дано отрицательное число!")
        else:
            root_num1(x, degree)


def summa_complex(x, y):
    print("Сумма равна:", x + y)


def dif_complex(x, y):
    print("Разность равна:", x - y)


def multiplication_complex(x, y):
    print("Произведение равно:", x - y)


def check_num(x, y):
    if x == y:
        print("Числа равны.")
    else:
        print("Числа не равны.")


def exponentiation_complex_num1(x, n):
    print("Возведение в степень равно:", x ** n)


def root_num1(x, n):
    print("Корень равен:", x ** (1./n))


if __name__ == '__main__':
    main()
