import sys # імпорт системного модуля, для виклику завершкння програми
from math import sqrt, factorial    # Імпортування двох конкретних функцій з модуля Math

print('Калькулятор v1.5')

# Інтерфейс калькулятора
Question = ('''
1. Додавання
2. Віднімання
3. Множення
4. Ділення
5. Корінь числа
6. Степінь
7. Факторіал
Q. Вихід''')

# Функція калькулятора
def calculator():
    print(Question)
    
    # Функція на перевірку введення цілого числа
    def int_from_str(prompt):
        while True:
            try:
                option = int(input(prompt))
            except ValueError:
                print('Ви вчинили з калькулятором нечемно, написавши не ціле число - тож не робіть такого =(')
            else:
                return option
            
    choice = input('Введіть матиматичну операцію: ')

    # Вибір математичної операції
    if choice in ['1', '2', '3', '4']:
        # Введення чисел
        N1 = int_from_str("Перше число: ")
        N2 = int_from_str("Друге число: ")
    elif choice in ['5', '6', '7']:
        # Введення числа
        N1 = int_from_str("Число: ")
    elif choice in ['Вихід', 'Q']:
        sys.exit([])
    else:
        print('Такої математичеої операції не існує!')
    
    # Сума чисел
    if choice == '1':
        print(f'{N1} + {N2} = {N1 + N2}')
    
    # Різниця чисел
    elif choice == '2':
        print(f'{N1} - {N2} = {N1 - N2}')

    # Множення чисел
    elif choice == '3':
        print(f'{N1} * {N2} = {N1 * N2}')

    # Ділення чисел
    elif choice == '4':
        if N2 == 0:
            print('На 0 ділити НЕ МОЖНА!!!')
        else:
            print(f'{N1} / {N2} = {N1 / N2}')

    # Квадратний корінь числа
    elif choice == '5':
        print(N1, '=', sqrt(N1))

    # Степінь числа
    elif choice == '6':
        print(N1, '=', (N1 ** 2))

    # Факторіал числа
    elif choice == '7':
        print(N1, '=', factorial(N1))

# Нескінченний цикл програми, допоки не буде виконана умова
def main():
    while True:
        calculator()
        choice = input('Бажаєте продовжити роботу з калькулятором? Якщо НІ, то напишіть Ні/Ніт або натисніть 0 ')
        if choice.lower() in ['0', 'н', 'ні', 'ніт', 'n', 'no', 'Q']:
            print("Написав калькулятор IRONKAGE")
            break

if __name__== "__main__":
    main()  