#1 Импортируйте библиотеку Numpy и дайте ей псевдоним np.

import numpy as np

#1 Создайте массив Numpy под названием a размером 5x2, то есть состоящий из 5 строк и 2 столбцов. 
#1 Первый столбец должен содержать числа 1, 2, 3, 3, 1, а второй - числа 6, 8, 11, 10, 7. 
#1 Будем считать, что каждый столбец - это признак, а строка - наблюдение. 
a = np.array([[1, 6],
             [2, 8],
             [3, 11],
             [3, 10],
             [1,7]])
print(a)
#1 Затем найдите среднее значение по каждому признаку, используя метод mean массива Numpy. 
#1 Результат запишите в массив mean_a, в нем должно быть 2 элемента.

mean_a = a.mean(axis=0)
print(mean_a)

#2Вычислите массив a_centered, отняв от значений массива “а” средние значения 
#соответствующих признаков, содержащиеся в массиве mean_a. 
#Вычисление должно производиться в одно действие. Получившийся массив должен иметь размер 5x2.
a_centered = np.subtract(a, mean_a)
print(a_centered)

#3Найдите скалярное произведение столбцов массива a_centered. 
#В результате должна получиться величина a_centered_sp.
a_centered_sp1 = a_centered[:,0]
a_centered_sp2 = a_centered[:,1]
a_centered_sp = a_centered_sp1 @ a_centered_sp2
print(a_centered_sp)

#Затем поделите a_centered_sp на N-1, где N - число наблюдений.
N = a.shape[0]
print(N)
b = a_centered_sp / (N-1)
print(b)

#Задание 1
#Импортируйте библиотеку Pandas и дайте ей псевдоним pd.

import pandas as pd

#Создайте датафрейм authors со столбцами author_id и author_name, 
#в которых соответственно содержатся данные: [1, 2, 3] и ['Тургенев', 'Чехов', 'Островский'].

a_2 = {
    "author_id": [1,2,3],
    "author_name": ['Тургенев', 'Чехов', 'Островский']}

authors = pd.DataFrame(a_2)
print(authors)

#Затем создайте датафрейм book cо столбцами author_id, book_title и price, в которых соответственно содержатся данные:
a_3 = {
       "author_id": [1, 1, 1, 2, 2, 3, 3],
       "book_title": ['Отцы и дети', 'Рудин', 'Дворянское гнездо', 'Толстый и тонкий', 'Дама с собачкой', 'Гроза', 'Таланты и поклонники'],
       "price": [450, 300, 350, 500, 450, 370, 290]}

book = pd.DataFrame(a_3)

print(book)

#Задание 2
#Получите датафрейм authors_price, соединив датафреймы authors и books по полю author_id.

authors_price = pd.merge(authors, book, on='author_id', how='inner')
print(authors_price)

#Задание 3
#Создайте датафрейм top5, в котором содержатся строки из authors_price с пятью самыми дорогими книгами

top5 = authors_price.nlargest(5, "price")
print(top5)

#Задание 4
#Создайте датафрейм authors_stat на основе информации из authors_price. В датафрейме authors_stat должны быть четыре столбца:
#author_name, min_price, max_price и mean_price,
#в которых должны содержаться соответственно имя автора, минимальная, максимальная и средняя цена на книги этого автора.
min_price = authors_price.groupby("author_name").agg({'price': 'min'}).rename(columns={'price':'min_price'})
max_price = authors_price.groupby("author_name").agg({'price': 'max'}).rename(columns={'price':'max_price'})
mean_price = authors_price.groupby("author_name").agg({'price': 'mean'}).rename(columns={'price':'mean_price'})


authors_stat = pd.concat([mean_price, min_price, max_price], axis = 1)
print (authors_stat)





