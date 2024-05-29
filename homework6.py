# Словари и  множества

my_dict ={"Ivan":1980,"Petr":1981,"Alex":2000}
print(my_dict)
print(my_dict.get("Ivan"))
print(my_dict.get("Anton"))
my_dict.update({"Anton":2004,"Sergey":1990})
print(my_dict)
my_dict.pop("Petr")
print(my_dict)

my_set ={1,2,3,2,4,3,1,5,"три","один", False ,}
list_ =set(my_set)
print(list_)
print(list_.add(6,))
print(list_.add(8))
print(list_.remove(2))
print(list_)



