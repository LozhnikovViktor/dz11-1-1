def get_numbers_from_user():
    """Запрашивает у пользователя список чисел и возвращает его в виде списка целых чисел"""
    while True:
        try:
            user_input = input("Введите список чисел через пробел: ")
            numbers = [int(num) for num in user_input.split()]
            return numbers
        except ValueError:
            print("Ошибка: введены некорректные данные. Пожалуйста, введите только целые числа через пробел.")

def find_max_value(numbers):
    """Находит максимальное значение в списке чисел"""
    if not numbers:
        return None
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num

def selection_sort(numbers):
    """Сортирует список чисел с использованием сортировки выбора"""
    for i in range(len(numbers)):
        min_index = i
        for j in range(i+1, len(numbers)):
            if numbers[j] < numbers[min_index]:
                min_index = j
        numbers[i], numbers[min_index] = numbers[min_index], numbers[i]
    return numbers

def count_occurrences(numbers, target):
    """Подсчитывает количество вхождений числа в список"""
    count = 0
    for num in numbers:
        if num == target:
            count += 1
    return count

def get_target_number(numbers):
    """Запрашивает у пользователя число для поиска"""
    while True:
        try:
            target = int(input("Введите число для поиска: "))
            return target
        except ValueError:
            print("Ошибка: введено некорректное число. Пожалуйста, введите целое число.")

def main():
    print("Программа для работы со списком чисел")
    print("-------------------------------------")

    # Получаем числа от пользователя
    numbers = get_numbers_from_user()

    # Находим максимальное значение
    max_num = find_max_value(numbers)
    print(f"\nМаксимальное значение в списке: {max_num}")

    # Сортируем список
    sorted_numbers = selection_sort(numbers.copy())  # Используем копию, чтобы не изменять оригинал
    print(f"Отсортированный список: {sorted_numbers}")

    # Подсчитываем количество вхождений числа
    target = get_target_number(numbers)
    occurrences = count_occurrences(numbers, target)
    print(f"Число {target} встречается {occurrences} раз(а) в списке.")

if __name__ == "__main__":
    main()
