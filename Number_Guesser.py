import random
import time

def user_guesser():
    print('Случайное число задано, теперь, попробуйте его угадать! После каждой \
неудачной попытки, вам будет дана подсказка, больше ли ваше предпологаемое число, или меньше.')
    targeted_number = random.randint(lower_limit, upper_limit + 1)
    guessed_number = 0
    while guessed_number != targeted_number:
        guessed_number = int(input())
        if guessed_number > targeted_number:
            print('Неверно, искомое число меньше того, что вы ввели: ')
        elif guessed_number < targeted_number:
            print('Неверно, искомое число больше того, что вы ввели: ')
        else:
            print('Вы угадали! Так держать!')

def computer_guesser():
    print('Загадайте число! Сейчас я попробую его отгадать.', 'У вас есть 5 секунд...', sep = '\n')
    guessed_number = random.randint(lower_limit, upper_limit)
    time.sleep(5)
    answear = 0
    while answear != 1:
        print(f'Вы загадали число {guessed_number}?', '1 - Да', '2 - Нет')
        answear = int(input())
        guessed_number = random.randint(lower_limit, upper_limit)
        if answear == 1:
            print('Ура! Приятно было с вами поиграть!')


print('Здравствуйте! Это игра "угадай число", пожалуйста, выберите, кто будет угадывать число: ')
print('1 - пользователь', '2 - компьютер', sep = '\n')
choise = int(input())

while choise != 1 and choise != 2:
    print('Ошибка! Введите корректное значение!')
    choise = int(input())

print('Пожалуйста, введите диапазон чисел(строго больше нуля), ')
lower_limit = int(input('Нижняя граница диапазона: '))
upper_limit = int(input('Верхняя граница диапазона: '))

while upper_limit <= lower_limit:
    print('Ошибка! Введите корректное значение!')
    lower_limit = int(input('Нижняя граница диапазона: '))
    upper_limit = int(input('Верхняя граница диапазона: '))
while True:
    if choise == 1:
        user_guesser()
        print('Хотите сыграть ещё?', '1 - Да', '2 - Нет', sep = '\n')
        contin = int(input())
        if contin == 2:
            print('Приятно было с вами поиграть!')
            break
        elif contin == 1:
            continue
    elif choise == 2:
        computer_guesser()
        print('Хотите сыграть ещё?', '1 - Да', '2 - Нет', sep = '\n')
        contin = int(input())
        if contin == 2:
            print('Приятно было с вами поиграть!')
            break
        elif contin == 1:
            continue