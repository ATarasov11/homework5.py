immutable_var = 56,18,32,'f','pink'#Кортеж является неизменяемой коллекцией, он не поддерживает обращение по элементам
print(immutable_var)
immutable_var = (56,18,32,'f','pink')
print(immutable_var)
immutable_var = tuple([56,18,32,'f','pink'])
print(immutable_var)
mutable_list = [(7,9),11,'black']
mutable_list [0] = 22
print(mutable_list)