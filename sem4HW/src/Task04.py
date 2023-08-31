from functools import reduce  # Функция для свёрки последовательности
from operator import mul  # Функция, перемножающая 2 числа

spisok = [16, 15, 9, 14, 13]  # Исходный список

result = reduce(mul, spisok)
#                    /\ Список для свёртки
#               /\ Используем умножение
#        /\ Сворачиваем контейнер
print(result)