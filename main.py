import random
import logging

list_greeting = ["Здравствуйте!", "Привет!", "Hola!"]
logging.basicConfig(filename="log_project.log", level=logging.DEBUG)


def main():
    random_word = random.choice(list_greeting)
    print(f"{random_word}, это ConsoleCalc!")
    print("Работаю с любыми арифметическими операторами." + "\n" + "Чтобы выйти, напишите quit")
    while(True):
        user_input = input("Введите математическую операцию (Например: 5+5)")
        if user_input == "quit":
            break
        result = CalculateOperation(user_input)
        print(f"Результат: {result}")
        


def CalculateOperation(param):
    if param[1] != "+" or "-" or "*" or "/" or "%":
        example = "Не поддерживаются цифры.Пишите числа"
    if param[1] == "+":
        example = int(param[0]) + int(param[2])
        logging.debug("The mathematical example is solved")
    elif param[1] == "-":
        example = int(param[0]) - int(param[2])
        logging.debug("The mathematical example is solved")
    elif param[1] == "*":
        example = int(param[0]) * int(param[2])
        logging.debug("The mathematical example is solved")
    elif param[1] == "/":
        example = int(param[0]) / int(param[2])
        logging.debug("The mathematical example is solved")
    elif param[1] == "%":
        example = int(param[0]) % int(param[2])
        logging.debug("The mathematical example is solved")
    return example



if __name__ == "__main__":
    main()

