# First, we will take the input: 
lower_value = int(input("ВВедите первое число: ")) 
upper_value = int(input("Введите вьорое число: ")) 
 
print("Простые числа: ") 
for number in range(lower_value, upper_value + 1): 
    if number > 1: 
        for i in range(2, number): 
            if(number % i) == 0: 
                break 
        else: 
            print(number) 
