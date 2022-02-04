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
#-

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
        [0,0,0,0],
        [0,0,0,0]
    ]
    for i in range(2):
        for j in range(4):
            if i == y1 and j == x1: print("♜", end = ' ')    #Ладья
            elif i == y2 and j == x2: print("♟", end = ' ')  #Жертва
            else: print(field[i][j], end = ' ')
        print()
    if (x1 == x2) or (x1 - 1 == x2) or (x2 - 1 == x1): print("YES") #Ням-ням
    else: print("NO")

####################
# Завдання 8. Слон #
####################
def elephant(x1, y1, x2, y2):
    x1-=1; y1-=1; x2-=1; y2-=1
    field = [
        [0,0,0,0],
        [0,0,0,0]
    ]
    for i in range(2):
        for j in range(4):
            if i == y1 and j == x1: print("♝", end = ' ')    #Слон
            elif i == y2 and j == x2: print("♟", end = ' ')  #Жертва
            else: print(field[i][j], end = ' ')
        print()
    if (x1 + 1 == x2 and y1 + 1 == y2) or (x1 - 1 == x2 and y1 + 1 == y2) or (x2 + 1 == x1 and y2 + 1 == y1) or (x2 - 1 == x1 and y2 + 1 == y1): print("YES")
    else: print("NO")



if __name__ == "__main__": 
    print("Use main.py, bla-bla-bla")
