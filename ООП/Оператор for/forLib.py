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
def digit_in_number(x, d):
    if 0 <= d and d <= 9:
        digits = []; val = 0
        while x > 0:
            digits.append(x % 10)
            x //= 10
        digits.reverse()
        for i in digits:
            if d == i: val += 1
        print(val)       
    
##########################
# Завдання 11. Сума цифр #
##########################
def sum_of_digits(x):
    sum = 0; digits = []
    while x > 0:
        digits.append(x % 10)
        x //= 10
    for i in digits:
        sum += i
    print(sum)
    
################################
# Завдання 12. Переверни число #
################################
def reverse_num(x):
    digits = []
    while x > 0:
        digits.append(x % 10)
        x //= 10
    #digits.reverse()
    for i in digits: print(i, end='')
    print()
    
####################################
# Завдання 13. Мінімальний дільник #
####################################
def min_div(x):
    min = 0
    for i in range(x+1):
        if i != 0 and i != 1 and x % i == 0 and min == 0: min = i
    print(min)

###############################
# Завдання 14. Дільники числа #
###############################
def all_div(x):
    for i in range(x+1):
        if i != 0 and x % i == 0: print(i, end=' ')
    print()

####################################
# Завдання 15. Кількість дільників #
####################################
def num_of_div(x):
    val = 0
    for i in range(x+1):
        if i != 0 and x % i == 0: val += 1
    print(val)

#########################
# Завдання 16. Сума ста #
#########################
def sum_of_hundred(x):
    if 100 <= x and x <= 999:
        digits = []; sum = 0
        while x > 0:
            digits.append(x % 10)
            x //= 10
        for i in digits: sum += i
        print(sum)

###########################
# Завдання 17. Сума чисел #
###########################
def sum_of_digits_again(x):
    if 100 <= x and x <= 999:
        digits = []; sum = 0
        while x > 0:
            digits.append(x % 10)
            x //= 10
        for i in digits: sum += i
        print(sum)
        
###############################
# Завдання 18. Переклад числа #
###############################
def binary_decimal(x): print(int(x, 2))

#####################
# Завдання 19. Нулі #
#####################
def zeroes(n1, n2, n3, n4):
    nums = [n1, n2, n3, n4]; value = 0
    for i in nums:
        if i == 0: value += 1
    print(value)

#################################
# Завдання 20. Підрахунок чисел #
#################################
def counting_numbers (n1, n2, n3, n4, n5, n6):
    nums = [n1, n2, n3, n4, n5, n6]
    valueZero = 0; valuePlus = 0; valueMinus = 0
    for i in nums:
        if i == 0: valueZero += 1
        elif i > 0: valuePlus += 1
        else: valueMinus += 1
    print(valueZero, valuePlus, valueMinus)
    
################################
# Завдання 21. Нуль чи не нуль #
################################
def zero_or_no(num1, num2, num3):
    thereszero = False
    nums = [num1, num2, num3]
    for i in nums:
        if i == 0: thereszero = True
    print(thereszero)
    
#######################################
# Завдання 22. Рівняння за зростанням #
#######################################
def equation_for_growth(a, b, c, d):
    thereissolution = False
    for x in range(1000):
        if a * x ** 3 + b * x ** 2 + c * x + d == 0: 
            print(x, end=' ')
            thereissolution = True
    if thereissolution == False: print("Нет решения")
    else: print()
    
######################################
# Завдання 23. Рівняння за спаданням #
######################################
def equation_for_descending(a, b, c, d):
    thereissolution = False
    solving = []
    
    for x in range(1000):
        if a * x ** 3 + b * x ** 2 + c * x + d == 0: 
            solving.append(x)
            thereissolution = True
            
    if thereissolution == False: print("Нет решения")
    else: 
        solving.reverse()
        for i in solving: print(i, end=' ')
    print()

#######################
# Завдання 24. ДНЧЕ-1 #
#######################
def DNCHE(seconds):
    digits = 0
    for nums in range(seconds):
        for i in range(nums):
            print(nums, end=' ')
            digits+=1
            if digits >= seconds: break 
        if digits >= seconds: break
    #print(f"\n\n{digits}") #проверка
    print()



if __name__ == "__main__": 
    print("Use main.py, bla-bla-bla")