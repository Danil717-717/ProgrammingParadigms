# Задача: Вычисление факториала
# Напишите программу, которая запрашивает у пользователя число n и вычисляет факториал этого числа с использованием цикла.

# def factorial(n):
#     result = 1
#     for i in range(1, n+1):
#         result *= i
#     return result

# n = int(input("Input num: "))
# result = factorial(n)
# print(f"Factorial num {n} = {result}")


#________________________________
# Функциональное программирование:
#Задача: Сумма квадратов четных чисел
#Напишите функцию, которая принимает список чисел и возвращает сумму квадратов четных чисел в списке, используя функциональные конструкции.

# def sum(numbers):
#     sum = 0
#     for num in numbers:
#         if num % 2 == 0:
#             sum += num**2
#     return sum

# n = [5, 6, 7, 4 ,6]
# print(sum(n))        

#______________________________
#Объектно-ориентированное программирование:
# Задача: Магазин и продукты
# Создайте классы Product и Store для моделирования магазина и продуктов. У магазина должны быть методы для добавления продуктов, отображения ассортимента и расчета общей стоимости покупки. Продукты могут иметь атрибуты, такие как название, цена и количество.

class Product:
    # name = name
    # price = price
    # quantity = quantity

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"{self.name} - {self.price}$ ({self.quantity} pcs)"    


class Store:

    def __init__(self):
        self.products = []
        
    def add_product(self, product):
        self.products.append(product)

    def display_products(self):
        print("Ассортимент магазина:")
        for product in self.products:
            print(f"{product.name} - Цена: {product.price} руб, Количество: {product.quantity}")

    def calculate_total(self, shopping_list):
        total_cost = 0
        for item in shopping_list:
            for product in self.products:
                if item["name"] == product.name:
                    total_cost += product.price * item["quantity"]
                break
        return total_cost

# Создание продуктов
product1 = Product("Яблоко", 50, 10)
product2 = Product("Молоко", 80, 5)
product3 = Product("Хлеб", 30, 8)

# Создание магазина и добавление продуктов
store = Store()
store.add_product(product1)
store.add_product(product2)
store.add_product(product3)

# Отображение ассортимента магазина
store.display_products()

# Список покупок
shopping_list = [
{"name": "Яблоко", "quantity": 3},
{"name": "Молоко", "quantity": 2},
{"name": "Хлеб", "quantity": 1}
]

# Расчет общей стоимости покупки
total_cost = store.calculate_total(shopping_list)
print(f"Общая стоимость покупки: {total_cost} руб.")



#Логическая парадигма

#Задача: Поиск числа в списке

#Условие: Дан список чисел. Напишите программу, которая проверяет, содержится ли заданное число в списке.

def search(num, count):
    if count in num:
        return True
    else:
        return False
    
numbers = [1, 2,3,4,5,6]
count = int(input())

if search(numbers, count):
    print("Yes")
else:
    print("No")    



