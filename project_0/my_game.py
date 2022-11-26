"""Игра угадай число.
Компьютер сам загадывает и угадывает число
"""

import numpy as np

def quick_predict(number: int = 1) -> int:
    """Быстрое угадывание числа

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0 # исходное число попыток равно 0

    # текущий диапазон загаданного числа:
    n_min = 1 # минимальное значение загаданного числа
    n_max = 101 # максимальное значение загаданного числа +1
    
    while True:
        count += 1 # увеличение счетчика попыток на 1
        predict_number = (n_min + n_max) // 2 # называем среднее между максимальным и минимальным (целочисленное деление)
        
        if number < predict_number:
            n_max = predict_number # если не угадали, а загаданное число меньше, то снижаем верхний интервал до загаданного
        elif number > predict_number:
            n_min = predict_number + 1 # если не угадали, а загаданное число больше, то снижаем нижний интервал до загаданного + 1
        elif number == predict_number:
            break  # если угадали, то выход из цикла
         
    return count


def score_game(predict_function) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        predict_function: функция угадывания

    Returns:
        score: среднее количество попыток
    """
    count_ls = [] # задание списка дла зяписи редультатов игры - количество попыток
    np.random.seed(123)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(quick_predict(number))

    score = round(np.mean(count_ls), 2)
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return score


if __name__ == "__main__":
    # RUN
    score_game(quick_predict)