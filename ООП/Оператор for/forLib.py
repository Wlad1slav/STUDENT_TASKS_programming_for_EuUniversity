import math

################
# Оператор for #
################

##############################
# Завдання 1. Сума квадратів #
##############################
def sumSq(n):
    n += 1
    if n <= 100: 
        for i in range(n): 
            if i > 0: print(str(i) + '2')
            
#########################
# Завдання 2. Факторіал #
#########################
def factorial(N):
    factor = 1; N += 2 #кастыль
    if N - 2 <= 12:
        for i in range(N):
            if i > 1: factor *= (i - 1)
            
    print(f"{N-2}! = {factor}")
    
#######################
# Завдання 3. Ступінь #
#######################
def power(N):
    pow = 1
    if pow <= 30:
        for i in range(N):
            pow *= 2
        print(pow)
            
##################################
# Завдання 4. 1/0!+1/1!+1/2!+... #
##################################
# def beliberda(N):
#     # sum = 1; factorial = 1; float(factorial); float(sum)
#     for i in range(N):
#         I = i + 2
#         # for fact in range(I):
#             # if fact > 1: factorial *= (fact - 1)
#             # print(factorial)
#         # sum += (1 / factorial)
#     print(sum)

#######################
# Завдання 5. Ступінь #
#######################
def power_again(a, n): print(a**n)

#########################
# Завдання 6. Факторіал #
#########################
def factorial_again(N):
    factor = 1; N += 2 #кастыль
    if N - 2 <= 12:
        for i in range(N):
            if i > 1: factor *= (i - 1)
            
    print(f"{N-2}! = {factor}")
    
###########################
# Завдання 7. Парні числа #
###########################
def even_numbers(a,b):
    if a < b:
        for a in range(b+1):
            if a % 2 == 0 and a != 0: print(a, end=' ')
        print() #чтобы путь к файлу выводился на следующей точке
    
#######################
# Завдання 8. Залишок #
#######################
def remainder(a, b, c, d):
    if a < b:
        for a in range(b+1):
            if a % d == c and a != 0: print(a, end=' ')
        print()

########################
# Завдання 9. Квадрати #
########################
def squares(a, b):
    if a < b:
        for a in range(b+1):
            if a != 0 and a != 1 and a % (a ** 0.5) == 0: print(a) #a ** 0.5 - корень числа

##############################
# Завдання 10. Цифра в числі #
##############################
#-




if __name__ == "__main__": 
    print("Use main.py, bla-bla-bla")