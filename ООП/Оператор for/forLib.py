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
            


if __name__ == "__main__": 
    print("Use main.py, bla-bla-bla")