# База знаний о родственных связях
father_of = {
('John', 'Alice'),
('John', 'Bob'),
('Michael', 'John'),
('Michael', 'Sara')
}

def uncle(x, y):
    return any((father, y) in father_of and (father, x) in father_of for father in father_of if (x, y) != father)

person_x = 'Alice'
person_y = 'Sara'

if uncle(person_x, person_y):
    print(f"{person_x} - дядя {person_y}")
else:
    print(f"{person_x} - не дядя {person_y}")





# База знаний об оценках студентов
grades = {
'Alice': [9, 8, 7, 9, 9],
'Bob': [6, 7, 6, 5, 7],
'Eve': [8, 9, 7, 8, 9],
'Mike': [5, 6, 4, 3, 5]
}

def excellent_student(student):
    return sum(grades[student]) / len(grades[student]) > 8

def struggling_student(student):
    return sum(grades[student]) / len(grades[student]) < 5

students = ['Alice', 'Bob', 'Eve', 'Mike']

for student in students:
    if excellent_student(student):
        print(f"{student} - отличник")
    elif struggling_student(student):
        print(f"{student} - нуждается в академической помощи")
    else:
        print(f"{student} - средний студент")    




#Задача: Напишем программу, которая проверяет, является ли заданное слово палиндромом. 

str = input("Введите слово")
if str==str[::-1]:
    print("Полиндром")
else:
    print("No polidrom") 


#Пусть у нас есть следующий текст:

#"Python is a powerful programming language. Python is used for web development, data analysis, machine learning, and more."

#Мы хотим подсчитать частоту встречаемости каждого слова в этом тексте.
#
# 
str =  "Python is a powerful programming language. Python is used for web development, data analysis, machine learning, and more."

str="Python is a powerful programming language. Python is used for web development, data analysis, machine learning, and more."
str.lower()
str=str.replace(".","")
str=str.replace(",","")
sp=str.split()

lib={}
for i in sp:
    if i in lib:
        lib[i]+=1
    else:
        lib[i]=1
print (lib)



#Задача: Напишем программу для анализа текста и определения самых часто встречающихся слов в нем.

str="Python is a powerful programming a language. Python is used for a web development, data a analysis, machine is learning, and more."
str.lower()
str=str.replace(".","")
str=str.replace(",","")
sp=str.split()

lib={}
for i in sp:
    if i in lib:
        lib[i]+=1
    else:
        lib[i]=1
# print (lib)

lib2 = sorted(lib.items(), key=lambda item: item[1],reverse=True)
print (lib2)


#Задача: Напишем программу, которая анализирует текст, определяет наиболее часто встречающиеся биграммы (пары последовательных слов) в нем.

#Machine learning is a subfield of artificial intelligence that focuses on the interaction between computers and humans. Machine learning involves the use of algorithms and statistical models to enable computers to perform tasks without explicit programming. In machine learning, data plays a crucial role. Data is used to train the algorithms and improve their performance over time. Machine learning has applications in various fields, including natural language processing, image recognition, and autonomous vehicles

#Мы хотим найти топ N наиболее часто встречающихся биграмм в этом тексте

str = "Machine learning is a subfield of artificial intelligence that focuses on the interaction between computers and humans. Machine learning involves the use of algorithms and statistical models to enable computers to perform tasks without explicit programming. In machine learning, data plays a crucial role. Data is used to train the algorithms and improve their performance over time. Machine learning has applications in various fields, including natural language processing, image recognition, and autonomous vehicles"
str=str.lower()
str=str.replace(".","")
str=str.replace(",","")
sp=str.split()
lib={}
for i in range (len(sp)-1):
    if (sp[i],sp[i+1]) in lib:
        lib[sp[i],sp[i+1]]+=1
    else:
        lib[sp[i],sp[i+1]]=1
n=int(input("Top skolko&: "))
lib2 = sorted(lib.items(), key=lambda item: item[1],reverse=True)
print (lib2[:n])






# Разделяем текст на слова, приводим к нижнему регистру и получаем список слов
words = text.lower().split()

# Создаем словарь для хранения пар слов и их количества
word_pairs = {}

# Проходим по списку слов с шагом 2, чтобы образовать биграммы
for i in range(len(words) - 1):
# Формируем биграмму из текущего слова и следующего слова
    word_pair = (words[i], words[i + 1])

# Если биграмма уже есть в словаре, увеличиваем счетчик
    if word_pair in word_pairs:
        word_pairs[word_pair] += 1
    else:
# Если биграммы нет в словаре, добавляем ее и устанавливаем счетчик в 1
        word_pairs[word_pair] = 1

# Проходим по словарю биграмм и их количества
for word_pair, count in word_pairs.items():
# Если количество больше 2, выводим биграмму и количество
    if count > 2:
        print(f"Word pair: {word_pair}, Count: {count}")
# Приводим текст к нижнему регистру
str = str.lower()

# Убираем точки и запятые
str = str.replace(".", "")
str = str.replace(",", "")

# Разбиваем текст на слова
sp = str.split()

# Создаем словарь для хранения пар слов и их количества
lib = {}

# Проходим по списку слов с шагом 1, чтобы формировать биграммы
for i in range(len(sp) - 1):
# Формируем биграмму из текущего слова и следующего слова
    word_pair = (sp[i], sp[i + 1])

# Если биграмма уже есть в словаре, увеличиваем счетчик
    if word_pair in lib:
        lib[word_pair] += 1
    else:
# Если биграммы нет в словаре, добавляем ее и устанавливаем счетчик в 1
        lib[word_pair] = 1

# Сортируем словарь по значению (количеству повторений) в обратном порядке
lib2 = sorted(lib.items(), key=lambda item: item[1], reverse=True)

# Выводим отсортированный список биграмм и их количества
print(lib2)