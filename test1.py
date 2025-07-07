# Запрашиваем данные
name = input("Введите ваше имя: ").strip()
surname = input("Введите вашу фамилию: ").strip()
age = input("Введите ваш возраст: ").strip()

# 1) Вывод c использованием метода format()
print("Ваше имя: {0}, Фамилия: {1}, Возраст: {2} лет.".format(name, surname, age))

# 2) Вывод c использованием f‑string
print(f"Ваше имя: {name}, Фамилия: {surname}, Возраст: {age} лет.")
