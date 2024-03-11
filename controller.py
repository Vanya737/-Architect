# controller.py
import model
import view

def run():
    while True:
        num1, operator, num2 = view.get_user_input()
        result = model.calculate(num1, num2, operator)
        view.display_result(result)
