user_name = input("Введите ваше имя: ")
print(f"Привет, {user_name}")
user_second_name = input("Введите вашу фамилию: ")
print(f"Хмм, супер, {user_second_name}. Теперь вам нужно придумать пароль ")
user_password = input("Введите новый пароль: ")
print(f"Отлично, теперь не забудьте свои данные, ваш пароль для авторищации: {user_password}")
password = input('Введите пароль: ')
access = False
if password == user_password:
    print('Пароль принят, вы успешно авторизовались')
    access = True
if password != user_password:
    print('Пароль неверен, введите снова')