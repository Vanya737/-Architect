# view.py

def display_result(result):
    print(f"Результат: {result}")

def get_user_input():
    num1 = float(input("Введите первое число: "))
    operator = input("Введите операцию (+, -, *, /): ")
    num2 = float(input("Введите второе число: "))
    return num1, operator, num2