# 5
# login = 'ivanova.ekaterina'
# password = input(login + ', введите пароль для входа в личный кабинет:')
# ok = password=='sweetstore111'
# print('Авторизация:',ok )

# 6
# category = input('Введите вид кондитерской продукции:')
# taste = input('Введите вкус:')
# category = category.lower()
# taste = taste.lower()
# is_top = category == 'торт' and taste == 'шоколадный'
# print('Задан самый популярный запрос:', is_top)

# 7
# category = input('Введите вид кондитерской продукции: ')
# price = int(input('Введите цену: '))
# category = category.lower()
# is_top = category == 'пирожные' and price <= 500
# print ('Предлагать продукцию по акции:',is_top)

# 4
# answer = input('Вы первый раз в Сладких историях?')
# answer = answer.lower()
# if answer == 'да':
#     print('Скидка 40% для новичков. Промокод NEW')
# else:
#     print('Торты со скидкой 10%. Промокод CAKE')

# 5
# max_price = int(input('Какую сумму вы готовы потратить на сладости?'))
# if max_price < 500:
#     print('Попробуйте пирожные со сгущенкой!')
# if max_price >= 500 and max_price <= 1000:
#     print('Побалуйте себя тортиком Секрет!')
# if max_price > 1000:
#     print('Угоститесь шоколадным фонданом с голубикой!')

# 6
# height = int(input('Введите ваш рост:'))
# weight = int(input('Введите ваш вес:'))
# if height - weight > 100:
#   print ('Ваш вес в норме. Может по круассану с кремом?')
# else:
#   print ('Избыточный вес!')

# 7
# age = int(input('Введите ваш возраст:'))
# if age < 30:
#   print ('Люди вашего возраста берут мороженое с фисташками')
#   print ('Переходите к покупкам!')
# else:
#   print ('Люди вашего возраста чаще берут темный шоколэйд')

# 8
# gang = int(input('Введите желаемый вес десерта в килограммах:'))
# if gang < 2:
#   print ('Попробуйте корзины со сливками!')
# elif gang >= 2 and gang <= 3:
#   print ('Как на счет ассорти мини-тортиков?')
# else:
#   print ('То рекомендуем многоярусный торт!')
# print ('Переходите к покупкам!')

#4
# sales = input('Желаете товары по акции?')
# if sales == 'да':
#     category = input('Введите категорию:')
#   print('Сообщите, если передумаете!')

#5
# category = input('Категория в разделе "Прямо с грядки":')
# if category == 'зелень':
#     max_price = int(input('Максимальная цена:'))
#     if max_price >= 100:
#         print('Попробуйте салатные миксы')
#     else:
#         print('Попробуйте ассорти из лука и петрушки')
# else:
#     print('Как насчёт батата?')

#6
# choice = input('Желайте изучить хиты продаж?:')
# if choice == 'да':
#   category = input('Интересующая категория:')
#   if category == 'Продукты':
#     print('Молоко 1л, Печенье с изюмом, Пресики')
#   else:
#     print('Стиральный порошок, Щётка для обуви')
# else:
#   print('Дайте знать если передумаете')

#7
# a = int(input('Цена первого товара:'))
# b = int(input('Цена второго товара:'))
# c = int(input('Цена третьего товара:'))
# if a > b > c:
#   print ('Наибольшая цена товара:', a)
# elif b > a > c:
#   print ('Наибольшая цена товара:', b)
# elif c > a > b:
#   print ('Наибольшая цена товара:', c)
# else:
#   print('Они равны')

#5
# category = input('Введите категорию:')
# if category == 'хит продаж':
#     print('Товар недели - виноград Киш-миш')
# elif category == 'веган':
#     print('Попробуйте спаржу с тофу!')
# else:
#     print('Как насчёт свиного шашлычка?')

#6
# sum = int(input('Сумма:'))
# time = int(input('Текущее время (час):'))
# total = sum/2
# if time >= 20 and time <= 22:
#   print('Акция! Итого к оплате:', total)
# elif time >=8 and time <=19:
#   print('Итого к оплате:', sum)
# else:
#   print('Магазин не работает!')