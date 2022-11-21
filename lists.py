# Создайте список из чисел 3, 5, 7, 9 и 10.5
# Выведите содержимое списка на экран
# Добавьте в конец списка строку "Python"
# Выведите длину списка на экран
list_numbers = [3, 5, 7, 9, 10.5]
print(list_numbers)
list_numbers.append("Python")
print(list_numbers)
print(len(list_numbers))

# Выведите на экран начальный элемент списка
# Выведите на экран последний элемент списка
# Напечатайте элементы списка со второго по четвертый включительно
# Удалите из списка строку "Python"
print(list_numbers[0])
print(list_numbers[-1])
print(list_numbers[1:4])
list_numbers.remove("Python")
print(list_numbers)
