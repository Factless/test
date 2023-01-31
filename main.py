def greet():
    print("------------------")
    print(" Приветствуем вас ")
    print("      в игре      ")
    print(" крестики-нолики  ")
    print("------------------")
    print(" формат ввода: x y")
    print(" x - номер строки ")
    print(" y - номер столбца")
greet()
def show():
    print()
    print("    |0|1|2| ")
    print("  _________ ")
    for i, row in enumerate(field):
        row_str = f"  {i} | {' | '.join(row)} | "
        print(row_str)
        print(" ______________ ")
    print()
def ask():
    while True:
        cords = input("     Ваш ход").split()

        if len(cords) != 2:
            print(" Введите 2 координаты!")
            continue

        x, y = cords

        if not(x.isdigit()) or not(y.isdigit()):
            print("Введите числа!")
            continue

        x, y =int(x), int(y)

        if 0 > x or 2 or 0 > y or y > 2 :
            print(" Координаты вне диапазона!")
            continue
        if field[x][y] != " ":
            print("Клетка занята!")
            continue
        return x, y

