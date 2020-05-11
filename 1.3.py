# 3. Сформувати функцію для обчислення індексу максимального елемента масиву
# n*n, де 1<=n<=5.
#Курдупов Олексій 122Г
import numpy as np#імпорт бібліотеки нампай
import random#імпорт рандом
while True:
    x = int(input('Введіть розмірність масиву від 1 до 5: ')) # Задання розміру масиву та ініціалізація
    if x > 5 or x < 0:        # перевірка на правильність введення
        print('Ведіть розмірність від 1 до 5')
        break
    else:
        Z = np.zeros((x, x), dtype=int)
    for i in range(len(Z)):#проходження по списку
        for j in range(len(Z)):#проходження по списку
            Z[i, j] = random.randint(-5, 10)
    print(Z)
    def elem_rec(array, I=0, J=0, i=0, j=0):#рекурсивне рішення.
        if J == len(array[I]):
            I += 1
            J = 0
        if I == len(array):
            return i, j
        if array[I][J] > array[i][j]:
            i = I
            j = J
        J += 1
        return elem_rec(array, I, J, i, j)
    print('Максимальний елемент 3 індексом(за рекурсивним рішенням): ', elem_rec(Z))
    def max_element(f):#ітераційне рішення.
        max_elem = f[0][0]
        for i in range(len(f)):#проходження по списку
            for j in range(len(f[i])):#проходження по списку
                if f[i][j] > max_elem:
                    max_elem = f[i][j]
        list_index = [(i, j) for i in range(len(f)) for j in range(len(f[i])) if f[i][j] == max_elem] # Знаходження індексу максимального рядка
        line, column = list_index[0]
        return line, column
    print('Максимальний елемент 3 індексом(за ітераційним рішенням): ', max_element(Z))


#У цій програмі ми також використовуємо два методи: ітераційний та рекурсивний.
#На мою думку у цій програмі краще використовувати рекурсивний метод розвязу.
#Він займає меньше місця, виконує меньше порівнянь та займає меньше часу.