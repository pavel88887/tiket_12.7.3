per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
#Получения список значений из словаря
list1=list(per_cent.values())

#Запрашиваем ввод суммы которую человек планирует положить под проценты.
money = float(input('Введите сумму для вклада:'))
#print('money =',int(money))

#Создаем пустой список и с помощью цикла добаляем в него накопленные средства за год вклада в каждом из банков
deposit=[]
for i in list1:
    deposit.append(round(money * i/100))
#print('deposit =',deposit)

#Выводим максимальную сумму при помощи функции max()
print('Максимальная сумма, которую вы можете заработать —',max(deposit))