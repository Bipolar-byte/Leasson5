tuple_immutable_var = "Food", 'Water', "2", "1", False
print(tuple_immutable_var)
#tuple_immutable_var[0] = 5
#print(tuple_immutable_var)
print("Неизменяемый кортеж не поддерживает обращение по элементам, Что оповешает нас, в если раскоментировать 3 и 4 строку!")
tuple_mutable_list = ["Food", 'Water', "2", "1", False]
print(tuple_mutable_list)
tuple_mutable_list[2] = 1
tuple_mutable_list[3] = 2
tuple_mutable_list[4] = True
print(tuple_mutable_list)


