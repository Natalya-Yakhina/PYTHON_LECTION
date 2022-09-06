#print("hello world")


# ========= Типы данных =========
# int, float, boolean, str, list и др.
#value = None
#a = 123
#b = 3.14
#print(type(a))  #type - функция для типа данных   \n - переход на новую строку
##print(type(b))
##value = 12332
##print(type(value))

# вывод + интерполяция
#a = 123
#b = 3.14
#print(a, "-", b)
#print("{1} - {2}" .format(a, b))
#print(f"{a} - {b}")

#list = [1, 2, 3]
#print(list)

#print() – отвечает за вывод данных
#input() – отвечает за ввод данных

#print("Введите a = ")
#a = int(input()) # если нужно целое число используем функцию int(input()), вещественных float
#print("Введите b = ")
#b = int(input())
#print(a, "+", b, "=", a+b)
#print("{} {}".format(a, b))
#print(f"{a} {b}")

# ===== Арифметические операции =====
# +, -,
#*, /, %, //,**
#Приоритет операций
#**, ⊕, ⊖,*, /, //, %, +, -
#( ) Скобки меняют приоритет

# ===== Сокращенные операции =====
#a = +123 #унарный плюс
#b = -321 #унарный минус
#c = a + b
#print(c)

#a = 12
#b = 3
#c = a / b  # // - если хочу в целых числах, % - остаток от деления, ** возведение в степень
#print(c)
# нет ограничений в хранении

#a = 1.312312
#b = 3
#c = round(a * b, 7)  # 3 - количество знаков, иначе округляет
#print(c)

# ===== Сокращенные операции присваивания =====
#a = 3
#a += 5
#print(a)

# ============ Логические операции =============
# >, >=, <, <=, ==, !=
# not, and, or – не путать с &, |, ^
# Кое-что ещё: is, is not, in, not in

#a = 1 < 4 and 5 > 2 #!= 2 
#print(a)

#a = "хуй"
# = "хуй"
#print(a == b)

#можно использовать двойные и четверные неравенства
#funk = 1
#T = 4
#x = 123
#print(funk < T > (x))

#f = 1 > 2 or 4 < 6
#print(f) 

#f = [1, 2, 3, 4]
#print(f)
#print(not 2 in f) # не содержит

#проверить четность числа
#is_odd = not f[0] % 2
#print(is_odd)


# =========  Управляющие конструкции: if, if-else  ============
# == 1 ==
# if condition:
 # operator 1
 # operator 2
 # ...
 # operator n
#else:
 # operator n + 1
 # operator n + 2
 # ...
 # operator n + m

# пример: максимум из двух чисел
#a = int(input("Введите a = "))4
#b = int(input("Введите b = "))
#if a > b: 
#    print(a)
#else:
#    print(b)

# === 2 ===
# if condition1:
 # operator
# elif condition2:
 # operator
# elif condition3:
 # operator
# else:
 # operator 

#username = input("Введите имя: ")
#if username == "Маша":
#    print("Ура, это же Маша")
#elif username == "Марина":
#    print("Я ждал Вас, Марина")
#elif username == "Ильнар":
#    print("Ильнар - топ")
#else:
#    print("Привет, ", username)

# 
# ======== Цикл позволяет выполнить блок операторов какоето количество раз =======
# while condition:
 # operator 1
 # operator 2
 # . . .
 # operator n

#перевернули число
#original = 23
#inverted = 0
#while original != 0:
#    inverted = inverted * 10 + (original % 10)
#    original //= 10
#print(inverted)

# =========== Управляющие конструкции: while-else ============= // когда основное тело цикла перестает работать
# while condition:
 # operator 1
 # operator 2
 # . . .
 # operator n
# else:
 # operator n + 1
 # operator n + 2
 # . . .
 # operator n + m

# original = 23
# inverted = 0
# while original != 0:
#     inverted = inverted * 10 + (original % 10)
#     original //= 10
# else:
#     print('Пожалуй')
#     print('хватит )')
#     print(inverted)

# ================ Управляющие конструкции: for ==========================
# for i in enumeration:
 # operator 1
 # operator 2
 # . . .
 # operator n

# for i in 1, -2, 3, 14, 5:
    #print(i)

# for i in range(1, 5):
#    print(i)

# ============  Немного о строках  =============
# help( text.istitle) // справка

#text = 'съешь ещё этих мягких французских булок'
# print(len(text)) # 39
# print('ещё' in text) # True
# print(text.isdigit()) # False
# print(text.islower()) # True
# print(text.replace('ещё','ЕЩЁ')) #
# for c in text:
#  print(c)

# text = 'съешь ещё этих мягких французских булок' #срез
# print(text[0]) # c
# print(text[1]) # ъ
# print(text[len(text)-1]) # к
# print(text[-5]) # б
# print(text[:]) # print(text) // [0:len(text)-1]
# print(text[:2]) # съ // от 0 до второго
# print(text[len(text)-2:]) # ок
# print(text[2:9]) # ешь ещё
# print(text[6:-18]) # ещё этих мягких
# print(text[0:len(text):6]) # сеикакл
# print(text[::6]) # сеикакл
# text = text[2:9] + text[-5] + text[:2] # ...

# =========== Списки: введение =============

# numbers = [1, 2, 3, 4, 5]
# print(numbers) # [1, 2, 3, 4, 5]
# numbers = list(range(1, 6))

# print(numbers) # [1, 2, 3, 4, 5]
# numbers[0] = 10
# print(f"{len(numbers)} len") # [10, 2, 3, 4, 5]
# print(numbers)
# for i in numbers:
#     i *= 2
#     print(i) # [20, 4, 6, 8, 10]
# print(numbers) # [10, 2, 3, 4, 5]


# colors = ['red', 'green', 'blue']
# for e in colors:
#  print(e) # red green blue
# for e in colors:
#  print(e*2) # redred greengreen blueblue
# colors.append('gray') # append = добавить в конец
# print(colors == ['red', 'green', 'blue', 'gray']) # True
# colors.remove('red') #del colors[0] # remove = удалить элемент

# ============= Функции ===============

# def function_name(x):
# body line 1
# . . .
# body line n
 # optional return

def f(x): # целое или нет
    if x == 1:
        return 'Целое'
    elif x == 2.3:
            return 23
    else:
        return

arg = 2
print(f(arg))
print(type(f(arg)))