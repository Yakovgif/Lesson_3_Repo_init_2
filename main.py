# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/













import random

mainLoop = True
answer = 0
startScore = 100
countInput = 0

while mainLoop:
    level = input('Выберите уровень сложности Легкий - 1, Средний - 2, Сложный- 3\n')
    if level == '1':
        digit = random.randint(10,20)
        startScore = 200
        start = 10
        end = 20
        print('Попробуй отгадать число в диапазоне от 10 до 20')

    elif level == '2':
        digit = random.randint(20,50)
        startScore = 150
        start = 20
        end = 50
        print('число в диапазоне от 20 до 50 Попробуйте отгадать')
    elif level == '3':
        digit = random.randint(50,100)
        startScore = 100
        start = 50
        end = 100
        print('число в диапазоне от 50 до 100 Попробуй отгадать')
    else:
        print('вы ввели неправильный уровень сложности попробуйте еще раз\n')
        continue
        print(digit)
    print(digit)
    countInput = 0 # переменная счетчик дл подсчета попыток
    # print('Компьютер загадал число Попробуй угадай')
    while answer != digit and startScore > 0:
        countInput += 1
        answer = input('\nВведите число : ')
        if not answer.isnumeric() or int(answer) < 10 or int(answer) > 20:
            print('ошибка ввода.Введите число от 10 до 20')

        elif answer.isnumeric() or int(answer) < 50 or int(answer) > 20:
            print('ошибка ввода.Введите число от 20 до 50')
            continue
        answer = int(answer)
        if answer == digit:
            print('Winner, You win')
        else:
            if countInput > 4 and countInput < 10:
                if countInput == 10:
                    print(f'у вас закончились очки.Компьютер загадал число {digit}')
                    break
                startScore -=10
                print('вы ошиблись угадайте дальше')
                print(f'у вас осталось {startScore} очков')
                if countInput > 6:
                    if startScore < 0:
                        print(f'увы у вас закончились очки компьютер загадал {digit}')
                        break
                    if digit % 2 == 0:
                        print('загадачное число четное')
                    else:
                        print('загадочное число нечетное')
                if answer > digit:
                    print('загадочное число Меньше вашего')
                    continue
                else:
                    print('загадочное число Больше вашего')
                    continue
            else:
                print('вы ошиблись угадывайте дальше: ')
                startScore -= 10
                print(f'у вас осталось {startScore} очков')
    if(input('\nНажми Enter если хочешь сыграть еше раз, если нет тогда 0 для выход') == '0'):
        print('\nспасибо что поиграли пока')
        mainLoop = False

































