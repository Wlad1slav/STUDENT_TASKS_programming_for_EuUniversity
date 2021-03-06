###############
#IF ELSE SWICH#
###############
######################################
# Завдання 1. Максимум із двох чисел #
######################################
def lagest_number(num1, num2):
    if num1 < num2: print(f"{num2} больше {num1}")
    elif num1 > num2: print(f"{num1} больше {num2}")
    else: print(f"{num1} равно {num2}")

##############################
# Завдання 2. Високосний рік #
##############################
def leap_year(year):
    if year % 400 == 0: print("YES")
    else: print("NO")

################################
# Завдання 3. Тестуюча система #
################################
# def test(num1, num2):
#     if (num1 == 1 and num2 == 1) or (num1 != 1 and num2 !=1 ): print("YES")
#     else: print("NO")

def test(num1, num2):
    if abs(num1) % 10 == abs(num2) or int(num1) / 10 == abs(num2) or abs(num1) == abs(num2) or abs(num2) % 10 == abs(num1) or int(num2) / 10 == abs(num1): print("YES")
    else: print("NO")

##########################
# Завдання 4. Знак числа #
##########################
def sign(x):
    if x > 0: x=1
    elif x < 0: x=-1
    else: x=0
    print(x)

###################################
# Завдання 5. Яке з чисел більше? #
###################################
def lagest_number_again(num1, num2):
    if num1 < num2: print("2")
    elif num1 > num2: print("1")
    else: print("0")

#################################
# Завдання 6. Максимум із трьох #
#################################
#Умный бы человек подключил бы модуль heapq и не парился
def lagest_number_of_three_digits(num1, num2, num3):
    if num2 < num1 > num3: print(num1)
    elif num1 < num2 > num3: print(num2)
    else: print(num3)

#####################
# Завдання 7. Ладья #
#####################
def rook(x1, y1, x2, y2):
    x1-=1; y1-=1; x2-=1; y2-=1 #костыль
    field = [
        [0,1,0,1,0,1,0,1],#8
        [1,0,1,0,1,0,1,0],#7
        [0,1,0,1,0,1,0,1],#6
        [1,0,1,0,1,0,1,0],#5
        [0,1,0,1,0,1,0,1],#4
        [1,0,1,0,1,0,1,0],#3
        [0,1,0,1,0,1,0,1],#2
        [1,0,1,0,1,0,1,0],#1
        #A B C D E F G H
    ]
    for i in range(8):
        for j in range(8):
            if i == y1 and j == x1: print("♜", end = ' ')    #Ладья
            elif i == y2 and j == x2: print("♟", end = ' ')  #Жертва
            else: print(field[i][j], end = ' ')
        print()
    if (x1 == x2) or (y1 == y2): print("YES") #Ням-ням
    else: print("NO")

####################
# Завдання 8. Слон # #Minute revelations, не сам понял, что нужен модуль числа
####################
def elephant(x1, y1, x2, y2):
    x1-=1; y1-=1; x2-=1; y2-=1
    field = [
        [0,1,0,1,0,1,0,1],#8
        [1,0,1,0,1,0,1,0],#7
        [0,1,0,1,0,1,0,1],#6
        [1,0,1,0,1,0,1,0],#5
        [0,1,0,1,0,1,0,1],#4
        [1,0,1,0,1,0,1,0],#3
        [0,1,0,1,0,1,0,1],#2
        [1,0,1,0,1,0,1,0],#1
        #A B C D E F G H
    ]
    for i in range(8):
        for j in range(8):
            if i == y1 and j == x1: print("♝", end = ' ')    #Слон
            elif i == y2 and j == x2: print("♟", end = ' ')  #Жертва
            else: print(field[i][j], end = ' ')
        print()
    if abs(x1 - x2) == abs(y1 - y2): print("YES")
    else: print("NO")

#####################
# Завдання 9. Ферзь #
#####################
def queen(x1, y1, x2, y2):
    x1-=1; y1-=1; x2-=1; y2-=1
    field = [
        [0,1,0,1,0,1,0,1],#8
        [1,0,1,0,1,0,1,0],#7
        [0,1,0,1,0,1,0,1],#6
        [1,0,1,0,1,0,1,0],#5
        [0,1,0,1,0,1,0,1],#4
        [1,0,1,0,1,0,1,0],#3
        [0,1,0,1,0,1,0,1],#2
        [1,0,1,0,1,0,1,0],#1
        #A B C D E F G H
    ]
    for i in range(8):
        for j in range(8):
            if i == y1 and j == x1: print("♛", end = ' ')    #Ферзь
            elif i == y2 and j == x2: print("♟", end = ' ')  #Жертва
            else: print(field[i][j], end = ' ')
        print()
    if (abs(x1 - x2) == abs(y1 - y2)) or ((x1 == x2) or (y1 == y2)): print("YES")
    else: print("NO")

#######################
# Завдання 10. Король #
#######################
def king(x1, y1, x2, y2):
    x1-=1; y1-=1; x2-=1; y2-=1
    field = [
        [0,1,0,1,0,1,0,1],#8
        [1,0,1,0,1,0,1,0],#7
        [0,1,0,1,0,1,0,1],#6
        [1,0,1,0,1,0,1,0],#5
        [0,1,0,1,0,1,0,1],#4
        [1,0,1,0,1,0,1,0],#3
        [0,1,0,1,0,1,0,1],#2
        [1,0,1,0,1,0,1,0],#1
        #A B C D E F G H
    ]
    for i in range(8):
        for j in range(8):
            if i == y1 and j == x1: print("♚", end = ' ')    #Король
            elif i == y2 and j == x2: print("X", end = ' ')  #Жертва
            else: print(field[i][j], end = ' ')
        print()
    if abs(x1 - x2) <= 1 and abs(y1 - y2) <= 1: print("YES")
    else: print("NO")

#####################
# Завдання 11. Конь #
#####################
def horse(x1, y1, x2, y2):
    x1-=1; y1-=1; x2-=1; y2-=1
    field = [
        [0,1,0,1,0,1,0,1],#8
        [1,0,1,0,1,0,1,0],#7
        [0,1,0,1,0,1,0,1],#6
        [1,0,1,0,1,0,1,0],#5
        [0,1,0,1,0,1,0,1],#4
        [1,0,1,0,1,0,1,0],#3
        [0,1,0,1,0,1,0,1],#2
        [1,0,1,0,1,0,1,0],#1
        #A B C D E F G H
    ]
    for i in range(8):
        for j in range(8):
            if i == y1 and j == x1: print("♞", end = ' ')    #Конь
            elif i == y2 and j == x2: print("X", end = ' ')  #Жертва
            else: print(field[i][j], end = ' ')
        print()
    if (x1 + 1 == x2 and y1 + 2 == y2) or (x1 - 1 == x2 and y1 + 2 == y2) or (x1 + 2 == x2 and y1 + 1 == y2) or (x1 - 2 == x2 and y1 + 1 == y2) or (x1 - 2 == x2 and y1 - 1 == y2) or (x1 + 2 == x2 and y1 - 1 == y2): print("YES")
    else: print("NO") 

##########################
# Завдання 12. Шоколадка #
##########################
def chocolate(N, M, K): #N x M - размер шоколада. K - кол-во квадратиков шоколадки
    if ((K % N == 0) or (K % M == 0)) and K < N * M: print("YES")
    else: print("NO")

######################
# Завдання 13. Фішки #
######################
def chips(chips):
    if (chips % 4 == 0): print("YES")
    else: print("NO")

#########################
# Завдання 14. Рівняння #
#########################
def equation(a, b): #a*x+b=0
    if (a == 0) or (b % a != 0): print("NO")
    elif a == 0 and b == 0: print("INF")
    else: print(-b / a)

#################################
# Завдання 15. Складне рівняння #
#################################
def complex_equation(a, b, c, d):
    if b % a == 0:
        print(-b / a)
    elif a == 0 and b == 0: print("INF")
    else: print("NO")

######################
# Завдання 16. Решта #
######################
def rest(price_rub, price_coins, paid_rub, paid_coins):
    if (paid_rub > price_rub) or ((paid_rub == price_rub) and (paid_coins > price_coins)):
        
        rest_rub = paid_rub - price_rub
        rest_coins = paid_coins - price_coins

        if rest_coins >= 100:   #конвертация копеек
            rest_rub += (rest_coins / 100)
            rest_coins %= 100

        print(int(rest_rub), rest_coins)

    else: print("None") #если цена выше оплаты
    
#########################
# Завдання 17. Морозиво #
#########################
def ice_cream(value):
    if value == 3 or value == 5: print("YES")
    else: print("NO")

########################
# Завдання 18. Котлети #
########################
def cutlets(k, m, n):
    if n * 2 % k == 0: time = m * (n * 2 / k)
    elif k >= n: time = m * 2
    else: time = m * ((n * 2 / k) + 1)
    print(time)

##########################################
# Завдання 19. Кількість рівних із трьох #
##########################################
def equality(num1, num2, num3):
    if num1 == num2 == num3: print('3')
    elif num1 != num2 != num3: print('0')
    else: print('2')

#######################
# Завдання 20. Корови #
#######################
def cows(n):
    if n < 100:
        if n % 10 == 1 and (n < 10 or n > 20): print(f"На лугу пасётся {n} корова")
        elif 4 >= (n % 10) >= 2 and (n < 10 or n > 20): print(f"На лугу пасётся {n} коровы")
        else: print(f"На лугу пасётся {n} коров")


if __name__ == "__main__": 
    print("Use main.py, bla-bla-bla")
    