#4
# time = int(input('Введите текущее время в часах:'))
# while time >= 10 and time < 24:
#     print('Мы открыты')
#     time = int(input('Введите текущее время в часах:'))
# print('Мы закрыты. Часы работы: с 10 до 24.')

#5
# while input('Введите промокод:') != 'life':
#   print('Промокод не действителен.')
# print ('Промокод принят.')

#6
# promokod = input('Введите промокод:')
# while promokod != 'health' and promokod != 'life':
#   print ('Этот промокод недействителен')
#   promokod = input('Введите промокод:')
# print ('Промокод верен')

#7
# popit = input ('Введите отзыв:')
# while popit != 'off':
#   print ('Спасибо за отзыв')
#   popit = input ('Введите отзыв:')
# print ('Закрыто')

#8
# popit = int(input('Стоимость товара:'))
# cost = 0
# while popit != 0:
#   cost += popit
#   print ('Продолжайте покупки')
#   popit = int(input('Стоимость товара:'))
# print ('Стоимость покупок: ', cost)

###################

#3
# pay = int ( input ('Введите номер карты:'))
# amount = 0
# while amount < 3:
#   amount += 1
#   pay = int ( input ('Введите номер карты:'))
#   print ('Поздравляем! Вы получили скидку 10%')
# print ('Скидки закончились')

#4
#Подсчёт категорий товаров
# category = input('Категория (end - завершить):')
# count = 0
# while category != 'end':
#   count += 1
#   category = input('Категория (end - завершить):')
#   print ('Категория:',category)
# print ('Всего категорий:',count)

#6
#автомат для выдачи талонов
# avto= int ( input ('Введите 0 - получите талон, 1- выключить аппарат:'))
# cost = 0
# while avto != 1:
#   if avto == 0:
#     cost += 1
#     print ('Номер талона',cost)
#   else:
#     print ('не туда сунул')
#   avto= int ( input ('Введите 0 - получите талон, 1- выключить аппарат:'))
# print ('найс')

############################
#4
# for gang in range(3):
#   bank = input('Введите предпочтение:')
#   print = ('Предпочтение учтено')
# print('Система рекомендации настроена!')

#1_6
# count = int(input('Число участников:'))
# for i in range(count):
#   name = input ('Введите имя:')
#   print("Добро пожаловать на сервер,",)
# print("Чат создан")

#1_7
# login = input('Введите логин:')
# error = '=&@?%_^:$;#№!*'
# for i in login :
#   if i in error:
#     print("Запрещенный символ:", i)

#1_8
# text = 'algo'
# for sign in text:
#   if sign == 'a':
#     print ('*')
#   elif sign == 'g':
#     print ('^')
#   elif sign == 'o':
#     break
#   else:
#     print(sign)

#1_9
# password = input('Введите пароль: ')
# alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

# for i in password:
#   for j in range(len(alphabet)):
#     if i.lower() == alphabet[j]:
#       print(j+1)
#       break

#1_10
# number = input('Введите 1 - рекомендация, off - завершить')
# while number != 'off':
#     if number == '1':
#         preference = input('Ваше настроение:')
#         if preference == 'весёлое':
#             print('Мультфильм Шрек')
#         else:
#             print('Мультфильм Алладин')
#     number = input('Введите 1 - рекомендация, off - завершить')

a = "10"
b = "15"

d = a + b
a = b
t = a + b
print(t)