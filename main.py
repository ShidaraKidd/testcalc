x = int(input("Первое число: "))
y = str(input("Введите действие: "))
z = int(input("Второе число: "))

if y == "+":
    y = x + z
elif y == "*":
    y = x * z
elif y == "/":
    y = x / z
elif y == "!":
    n = 1
    for i in range(1, x + 1):
        n *= i
        print("Для", i, "!", "=", n)
        y = n
elif y == "-":
    y = x - z
elif y == "^":
    y = x ** z
print("Ваш ответ: " + str(y))
returnn = str(input("Продолжить? y/n "))
while returnn == "n":
    break
while returnn == "y":
    x = int(input("Первое число: "))
    y = str(input("Введите действие: "))
    z = int(input("Второе число: "))

    if y == "+":
        y = x + z
    elif y == "*":
        y = x * z
    elif y == "/":
        y = x / z
    elif y == "!":
        n = 1
        for i in range(1, x + 1):
            n *= i
            print("Для", i, "!", "=", n)
            y = n
    elif y == "-":
        y = x - z
    elif y == "^":
        y = x ** z
    print("Ваш ответ: " + str(y))
    returnn = str(input("Продолжить? y/n "))