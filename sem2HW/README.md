## Урок 2. Структурное и процедурное программирование на практике
Структурное программирование:
__
Трассировка пути в лабиринте:
__
Описание: Имеется двумерный массив, представляющий лабиринт, где '0' - это проход, а '1' - это стена. Начальная и конечная точки заданы. Необходимо определить путь от начальной до конечной точки.
Почему это структурное программирование: Задача может быть решена с помощью последовательных шагов, ветвлений (проверка на наличие стены или уже посещенной клетки) и циклов (для обработки всех возможных направлений движения).
Процедурное программирование:
__
Разбиение массива на подмассивы:
__
Описание: Имеется массив чисел. Необходимо разбить его на подмассивы так, чтобы сумма чисел в каждом подмассиве была меньше или равна заданному значению X.
Почему это процедурное программирование: Можно создать процедуру, которая будет принимать массив и значение X, а затем последовательно формировать подмассивы, следуя определенной логике. Это позволяет выделить процесс создания каждого подмассива в отдельную подпрограмму, делая основной код более чистым и понятным.
__
Рекурсивное вычисление чисел Фибоначчи:
__
Описание: Написать функцию, которая возвращает n-тое число Фибоначчи.
Почему это процедурное программирование: Здесь мы можем использовать рекурсивную процедуру, где каждый вызов функции делает два дополнительных вызова (для n-1 и n-2). Хотя это не самый эффективный способ решения, он хорошо демонстрирует концепцию процедурного программирования.
__
Эти задачи служат хорошими примерами того, как структурное и процедурное программирование может быть применено в реальных сценариях

__

**Структурное программирование:
Трассировка пути в лабиринте:**
__
Задание: Создайте функцию, которая принимает двумерный массив (лабиринт) и начальную и конечную точки. Функция должна возвращать путь от начальной до конечной точки или сообщение, что путь невозможен.
Входные данные:
Двумерный массив размера MxN, где '0' - это проход, а '1' - это стена.
Координаты начальной и конечной точки.
Выходные данные:
Массив координат пути или сообщение об ошибке.

**Процедурное программирование:
Разбиение массива на подмассивы:**
__
Задание: Напишите функцию, которая принимает массив чисел и значение X. Функция должна возвращать массив подмассивов так, чтобы сумма чисел в каждом подмассиве была меньше или равна X.
Входные данные:
Массив чисел длиной N.
Число X.
Выходные данные:
Массив подмассивов.
__
Рекурсивное вычисление чисел Фибоначчи:
__
Задание: Напишите рекурсивную функцию для вычисления n-того числа Фибоначчи.
Входные данные:
Число n.
Выходные данные:
n-тое число Фибоначчи.