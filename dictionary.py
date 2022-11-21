# Создайте словарь:
# {"city": "Москва", "temperature": "20"}
# Выведите на экран значение ключа city
# Уменьшите значение "temperature" на 5
# Выведите на экран весь словарь
dictionaty_weather = {
    "city": "Москва", 
    "temperature": "20"
}
print(dictionaty_weather["city"])
dictionaty_weather["temperature"] = int (dictionaty_weather["temperature"] ) - 5 
print(dictionaty_weather["temperature"])
print(dictionaty_weather)

# Проверьте, есть ли в словаре ключ country
# Выведите значение по-умолчанию "Россия" для ключа country
# Добавьте в словарь элемент date со значением "27.05.2019"
# Выведите на экран длину словаря
print(dictionaty_weather.get("country","Россия"))
dictionaty_weather["date"] = "27.05.2019"
print(dictionaty_weather)
print(len(dictionaty_weather))