# Данные, функции и модули в python
# 
# ++++++++++++++++ Файлы +++++++++++++++
# Хранение данных
# Передача данных в клиент-серверных проектах
# Хранение конфигов
# Логирование действий

# +++++++++++++++ Как работать с файлами: +++++++++++++++
# Связать файловую переменную с файлом,
# определив модификатор работы
# a – открытие для добавления данных
# r – открытие для чтения данных
# w – открытие для записи данных (старые удаляются, новые записываются)
# w+, r+

#===============================================================================================
# with open('file.txt', 'w') as data:
#   data.write('line 1\n')
#   data.write('line 2\n')


# colors = ['red', 'green', 'blue'] # список в качестве данных
# data = open('file.txt', 'w') # связваем текстовую переменную с текстовым файлом (путь, мод)
# data.writelines(colors) # разделителей не будет (writelines - функционал записи)
# data.write('\nline 2\n')
# data.write('\nline 3\n')
# data.close() # разорвать файловое подключение файла на диске

# чтение данных из файла
# path = 'file.txt'
# data = open(path, 'r')
# for line in data:
#     print(line)
# data.close()
# exit()
#===============================================================================================
# with open('file.txt', 'w') as data:
#     data.write('line 1\n')
#     data.write('line 2\n')
#     colors = ['red', 'green', 'blue']
#     data = open('file.txt', 'a')
#     data.writelines(colors) # разделителей не будет
#     data.close()
#     path = 'file.txt'
#     data = open(path, 'r')
#     for line in data:
#         print(line)
#         data.close()

# ===================== ФУНКЦИИ =============================

# Это фрагмент программы, используемый многократно

# def function_name(x):
# # body line 1
# # . . .
# # body line n
#  # optional return

# import hello as h # псевдоним
# print(h.f(1))

# значение по умолчанию для функции

# def new_string(symbol, count = 3): 
#     return symbol * count

# print(new_string('!', 5)) # !!!!!
# print(new_string('!')) # TypeError missing 1 required ...если не присвоить count
# print(new_string(4)) # 12

# возможность передачи нограниченного количества элементов

# def concatenatio(*params): # перед описанием ставится звездочка
#     res: str = "" # переменная: тип данных
#     for item in params:
#         res += item
#     return res

# print(concatenatio('a', 's', 'd', 'w')) # asdw
# print(concatenatio('a', '1', 'd', '2')) # a1d2
# # print(conatenatio(1, 2, 3, 4)) # TypeError: ...

# ===================================== РЕКУРСИЯ =====================================
# вызывает сама себя

# def fib(n):
#     if n in [1, 2]:
#         return 1
#     else:
#         return fib(n-1) + fib(n-2)
# list = []
# for e in range(1, 10):
#     list.append(fib(e))
# print(list) # 1 1 2 3 5 8 13 21 34

# ===================================== КОРТЕЖИ =====================================
# Кортеж – это неизменяемый “список”
# a = (3, 4)
# print(a)
# print(a[0])

# -----------------------------------------
# t = ()
# print(type(t)) # tuple
# t = (1,)
# print(type(t)) # tuple
# t = (1)
# print(type(t)) # int
# t = (28, 9, 1990)
# print(type(t)) # tuple
# colors = ['red', 'green', 'blue']
# print(colors) # ['red', 'green', 'blue']
# t = tuple(colors)
# print(t) 

# -----------------------------------------
# t = tuple(['red', 'green', 'blue'])
# print(t[0]) # red
# print(t[2]) # blue
# # print(t[10]) # IndexError: tuple index out of range
# print(t[-2]) # green
# # print(t[-200]) # IndexError: tuple index out of range
# for e in t:
#  print(e) # red green blue
# t[0] = 'black' # TypeError: 'tuple' object does not support
# item assignment

# -----------------------------------------
# распаковать кортеж в отдельную переменную

# t = tuple(['red', 'green', 'blue'])
# red, green, blue = t 
# print('r:{} g:{} b:{}'.format(red, green, blue))
# # r:red g:green b:blue

# ===================================== СЛОВАРИ =====================================
# Неупорядоченные коллекции произвольных объектов с доступом по ключу

# dictionary = {} # пустой словарь
# dictionary = \ # указание пар
#     {
#         'up': '↑',
#         'left': '←',
#         'down': '↓',
#         'right': '→'
#     }
# print(dictionary) # {'up':'↑', 'left':'←', 'down':'↓', 'right':'→'}
# print(dictionary['left']) # ←
# # типы ключей могут отличаться

# # -----------------------------------------получить все ключи или все значения -----------------------------------------
# for k in dictionary.keys():
#     print(k)

# for v in dictionary:
#     print(dictionary[v])


# # -----------------------------------------
# print(dictionary['up']) # # ----------------------------------------- ↑
# # типы ключей могут отличаться
# dictionary['left'] = '⇐'
# print(dictionary['left']) # # ----------------------------------------- ⇐
# #print(dictionary['type']) # KeyError: 'type'
# del dictionary['left'] # # ----------------------------------------- удаление элемента
# for item in dictionary: # for (k,v) in dictionary.items():
#  print('{}: {}'.format(item, dictionary[item]))
# # up: ↑
# # down: ↓
# # right: →

# ===================================== МНОЖЕСТВА =====================================
# Неупорядоченная совокупность элементов

# a = {1, 2, 3, 5, 8}
# b = {'2', '5', 8, 13, 21}
# print(type(a)) # set
# print(type(b)) # set

# colors = {'red', 'green', 'blue'}

# print(colors) # {'red', 'green', 'blue'}
# colors.add('red')
# print(colors) # {'red', 'green', 'blue'}
# colors.add('gray')
# print(colors) # {'red', 'green', 'blue','gray'}
# colors.remove('red')
# print(colors) # {'green', 'blue','gray'}
# # colors.remove('red') # KeyError: 'red' удалить значение
# colors.discard('red') # ok
# print(colors) # {'green', 'blue','gray'}
# colors.clear() # { } очистить множества
# print(colors) # set()

# -----------------------------------------
# создание множества на основе имеющегося
# a = {1, 2, 3, 5, 8}
# b = {2, 5, 8, 13, 21}
# c = a.copy()                # c = {1, 2, 3, 5, 8}
# u = a.union(b)              # u = {1, 2, 3, 5, 8, 13, 21}
# i = a.intersection(b)       # i = {8, 2, 5}
# dl = a.difference(b)        # dl = {1, 3}
# dr = b.difference(a)        # dr = {13, 21}
# q = a \
#         .union(b) \
#         .difference(a.intersection(b))
# {1, 21, 3, 13}

# -----------------------------------------
# неизменяемые множества

# a = {1, 2, 3, 5, 8}
# b = frozenset(a)
# print(b) # frozenset({1, 2, 3, 5, 8})

# ===================== СПИСКИ =============================

# list1 = [1, 2, 3, 4]
# list2 = list1

# for e in list1:
#     print(e)
# print()
# for e in list2:
#     print(e)

# list1[0] = 123 # поменяю значение
# list2[1] = 333

# print()

# for e in list1:
#     print(e)

# print()

# for e in list2:
#     print(e)

# # -----------------------------------------
# # удалить последний элемент нашего списка

# list1 = [1, 2, 3, 4]

# print(len(list1))
# print(list1.pop(2)) # номер элемента который удаляем
# print(list1)
# print(list1.pop())
# print(list1)
# print(list1.pop())
# print(list1)

# -----------------------------------------
# вставить элемент

list1 = [1, 2, 3, 4]

print(len(list1))
print(list1.insert(2, 11)) # номер элемента который вставляем (позиция, значение) append - добавление в конец
print(list1)




