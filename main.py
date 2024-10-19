# Напишите программу, которая принимает на ввод целое число в диапазоне
# от 1 до 5, и выводит соответствующее ему слово на английском языке.
def insert_word(word):
    print(f"Соответствующее слово: {word}")


try:
    number = int(input("Введите число от 1 до 5: "))
    if number == 1:
        insert_word("One")
    elif number == 2:
        insert_word("Two")
    elif number == 3:
        insert_word("Three")
    elif number == 4:
        insert_word("Four")
    elif number == 5:
        insert_word("Five")
    else:
        print("Некорректный ввод")
except ValueError:
    print("Ввод нечислового значения")
finally:
    print("Завершение работы программы")
