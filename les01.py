# coding : utf-8
import os
import psutil
import sys
# Коментарий
print("Самая крутая программа")
print("Привет, программист!")
name = input("Ваше имя: ")

print(name, ", добро пожаловать в мир Python!")

answer = input("Давайте поработает? (Y/N)")

# PEP-8
if answer == 'Y':  # список вопросов 1) Написать программу 2) Написать игру
    print("Что именно вы хотите?")
    print("[1] - выведу список файлов"
    print("[2] - выведу информацию о системе")
    do = int(input("Укажите номер действия"))
    if do == 1:
        print(os.getcwd())
        print(sys.platform)
        print(sys.getfilesystemencoding())
        print(os.getlogin())
        print(psutil.cpu_count())

    elif do == 2:
        print("Игроман")
elif answer == 'N':
    print("До свидания")
else:
    print("Неизвестный ответ")
