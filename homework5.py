# неизменяемые и изменяемыу обьекты
immutable_var = (1, 2, 3, 'четыре', 'пять', True)
print(immutable_var)
#immutable_var[2] = 4
#print(immutable_var)
#line 4, in <module>
#   immutable_var[2] = 4
#   ~~~~~~~~~~~~~^^^TypeError: 'tuple' object does not support item assignment
#кортеж не поддерживает обращение по элементам.

immutable_list = [1, 2, 3, "четыре" ,"пять" , True]
immutable_list[1] = 0
immutable_list[5] = False
immutable_list[3] = "три"
print(immutable_list)