#4
# feedback1 = input('Оставьте отзыв о путешествии:')
# length = len (feedback1)
# print('Спасибо за подробный отзыв! В нём целых', length, 'символов!')

#5
# feedback = 'Корпуcа 2, 7 и 9 - самые уютные! Если выберете этот отель, то останавливайтесь в них'
# building1 = feedback[8]
# building2 = feedback[11]
# building3 = feedback[15]
# print('Клиенты выбирают корпуса:', building1, building2, building3)

#6
# feedback = ('Вид на море - это фишка отеля!')
# feedback_advert = feedback[0:11]
# print('Нашим клиентам нравится:', feedback_advert)

#7
# feedback = 'Волшебный Отель с супер ресторанами. Лучший на Кипре. Качественная еда, большое разнообразие. Прекрасный пляж и сервис. Чистые и просторные номера! Все на пять! Японская кухня оставляет приятное впечатление. Всегда, приезжая в Лимассол, заказываем суши и роллы. Мимо витрины со сладким очень сложно пройти не остановившись, хотя бы посмотреть. Тихий район - это круто!'

# searching1 = 'тихий район'
# searching2 = 'вкусно'

# feedback_low = feedback.lower()

# result1 = feedback_low.find(searching1)
# result2 = feedback_low.find(searching2)

# print(searching1, result1)
# print(searching2, result2)

#5
# city = input('Введите город:')
# district = input('Введите район:')
# rating = input('Введите рейтинг:')
# searching = city+'/'+district+'/'+rating
# print('Запрос', searching, 'сформирован')

#7
# feedback = 'Алиса и Вася, большое спасибо за теплый приём!'
# name1 = feedback[0:5]
# name2 = feedback[8:12]
# total=name1+'/'+name2
# print('Назначить премию:', total)

#8
# restor = input('Насколько вы оцениваете отдых от 1 до 5:')
# poret=input('Что вам не понравилось?')
# total=restor+'-'+poret
# print(total)

print('Общий вес багажа:', int(input('Вес чемодана')) + int(input('Вес ручной клади')) + int(input('Вес доп. предметов')))