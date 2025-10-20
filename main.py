import random
import logging

list_greeting = ["Здравствуйте!", "Привет!", "Hola!"]
logging.basicConfig(filename="log_project.log", level=logging.DEBUG)

def main():
    random_word = random.choice(list_greeting)
    print(f"{random_word}, это ConsoleCalc!")
    print("Работаю с любыми арифметическими операторами." + "\n" + "Чтобы выйти, напишите quit")
    while(True):
        user_input = input("Введите математическую операцию (Например: [Первое число] [оператор] [Второе число])")
        if user_input == "quit":
            break
        result = CalculateOperation(user_input)
        print(f"Результат: {result}")
        


def CalculateOperation(param):
    try:
        formatted_text = param.split(" ")
        dirtyList = [formatted_text[0], formatted_text[2]]
        list_index = list(map(int, dirtyList))
        if formatted_text[1] == "+":
            result = list_index[0] + list_index[1]
        elif formatted_text[1] == "-":
            result = list_index[0] - list_index[1]
        elif formatted_text[1] == "*":
            result = list_index[0] * list_index[1]
        elif formatted_text[1] == "/":
            result = list_index[0] / list_index[1]
        elif formatted_text[1] == "%":
            result = list_index[0] % list_index[1]
        return result
    except IndexError:
        return "Напишите пример по шаблону"
    except ValueError:
        return "Только цифры и числа, но не буквы и слова"


if __name__ == "__main__":
    main()

