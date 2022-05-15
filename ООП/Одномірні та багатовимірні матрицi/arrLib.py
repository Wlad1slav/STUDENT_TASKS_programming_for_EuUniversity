def pairNumber(digits, result = ""):
    print("Завдання 1:", end=' ')
    Arr = str(digits).split(' ')
    if 1 <= len(Arr) and len(Arr) <= 100:
        num = 0
        for element in Arr:
            if num % 2 == 0: result += element + " "
            num += 1
        return result

def pairElements(digits, result = ""):
        print("Завдання 2:", end=' ')
        Arr = str(digits).split(' ')
        if 1 <= len(Arr) and len(Arr) <= 100:
            for element in Arr:
                if int(element) % 2 == 0: result += element + " "
            return result

def plusElements(digits, result = 0):
        print("Завдання 3:", end=' ')
        Arr = str(digits).split(' ')
        if 1 <= len(Arr) and len(Arr) <= 10000:
            for element in Arr:
                if int(element) > 0: result += 1
            return result

def moreThanPrevious(digits, result = 0):
        print("Завдання 4:", end=' ')
        Arr = str(digits).split(' ')
        if 1 <= len(Arr) and len(Arr) <= 10000:
            num = 0
            while num < len(Arr):
                if num > 0:
                    if int(Arr[num]) > int(Arr[num-1]): result += 1
                num += 1
            return result

def someSings(digits, result = ""):
        print("Завдання 5:", end=' ')
        Arr = str(digits).split(' ')
        if '0' not in Arr:
            if 1 <= len(Arr) and len(Arr) <= 10000:
                num = 0
                while num < len(Arr):
                    if num > 0:
                        if (int(Arr[num-1]) > 0 and int(Arr[num]) > 0) or (int(Arr[num-1]) < 0 and int(Arr[num]) < 0): 
                            result = "YES"
                            break
                        else: result = "NO"
                    num += 1
                return result
            else: return "Кількість елементів поза точкою визначення"
        else: return "У масиві є нуль!"

def moreThanTwoPrevious(digits, result = 0):
        print("Завдання 6:", end=' ')
        Arr = str(digits).split(' ')
        if 1 <= len(Arr) and len(Arr) <= 100:
            num = 0
            while num < len(Arr):
                if num > 0 and num < int(len(Arr))-1:
                    if int(Arr[num]) > int(Arr[num-1]) and int(Arr[num]) > int(Arr[num+1]): result += 1
                num += 1
            return result

def flipArray(digits, result = ""):
        print("Завдання 7:", end=' ')
        Arr = str(digits).split(' ')
        if 1 <= len(Arr) and len(Arr) <= 35:
            num = -1
            while num >= (len(Arr)*-1):
                result += Arr[num] + " "
                num -= 1
            return result

def maxElement(digits, result = 0):
        print("Завдання 10:", end=' ')
        Arr = str(digits).split(' ')
        if 1 <= len(Arr) and len(Arr) <= 35:
            first = True
            for element in Arr:
                if first == True: 
                    result = int(element)
                    first = False
                else: 
                    if result < int(element): result = int(element)
            return result

def someElement(digits):
        print("Завдання 11:", end=' ')
        Arr = str(digits).split(' ')
        if 1 <= len(Arr) and len(Arr) <= 35:
            first = True
            for element in Arr:
                if first == True: 
                    previus = [element]
                    first = False
                if element not in previus: previus.append(element) 
            return len(previus)

def line(digits):
        print("Завдання 11:", end=' ')
        Arr = str(digits).split(' ')
        if 1 <= len(Arr) and len(Arr) <= 35:
            first = True
            for element in Arr:
                if first == True: 
                    previus = [element]
                    first = False
                if element not in previus: previus.append(element) 
            return len(previus)

def lineArr(petja_height):
    print("Завдання 12:", end=' ')
    line = [165, 163, 160, 160, 157, 157, 155, 154]
    petja_found_place = False
    for person_height in line:
        if petja_height > person_height and petja_height != person_height and petja_found_place == False: 
            line.insert(line.index(person_height), petja_height)
            petja_found_place = True

    return line.index(petja_height) + 1

def balls(digits, result = 0):
    print("Завдання 15:", end=' ')
    Arr = str(digits).split(' ')
    prev = ""; volume = 1
    for element in Arr:
        if prev != element: 
            prev = element
            volume = 1
        else: volume += 1

        if volume == 3: result += 3
        elif volume > 3: result += 1

    return result

def digionalArr(height, result = "\n"):
    print("Завдання 16:", end=' ')
    
    array = [0] * height
    for i in range(height): array[i] = [0] * height # створення матриці
    for i in range(height): array[i][height-i-1] = 1 # права діагональ

    for i in range(height): # двійки
        array[i][height-i-1] = 1
        for j in range(height):
            if i + j >= height: array[i][j] = 2

    for i in array: # виведення матриці
        for j in i: result += str(j)
        result += "\n"
    return result

def symmetricalArray(no = False):
    array = [
        [0, 1, 2],
        [1, 0, 3],
        [2, 3, 0]
    ]
    print("Завдання 17:", end=' ')
    for i in range(3):
        for j in range(3):
            if array[i][j] == array[j][i]: pass
            else: no = True

    if no == True: return "no"
    else: return "yes"

def IIcompetition():
    array = [
        [3, 1, 2],
        [1, 3, 4],
        [3, 3, 3]
    ]
    print("Завдання 19:", end=' ')
    max = 0; coordinations = 0
    for i in range(3):
        for j in range(3):
            if array[i][j] > max:
                max = array[i][j]
                coordinations = f"{i} {j}"
    return f"{max} | {coordinations}"

def IIIcompetition():
    array = [
        [1, 5, 7],
        [1, 3, 5],
        [4, 1, 6]
    ]
    print("Завдання 20:", end=' ')

    max = 0; coordinations = 0
    for i in range(3):
        sum = 0
        for j in range(3): sum += array[i][j]
        if sum > max: 
            max = sum
            coordinations = f"{i}"

    return coordinations

def IVcompetition():
    array = [
        [3, 1, 2],
        [1, 3, 4],
        [4, 4, 0]
    ]
    print("Завдання 21:", end=' ')

    max = 0; winners = 1
    for i in range(3):
        sum = 0
        for j in range(3): sum += array[i][j]
        if sum > max: 
            max = sum
            winners = 1
        elif sum == max: winners += 1

    return winners

def Vcompetition():
    array = [
        [4, 4, 0],
        [1, 2, 4],
        [4, 4, 0]
    ]
    print("Завдання 22:", end=' ')

    max = 0; winners = 1; coordinations = ""
    for i in range(3):
        sum = 0
        for j in range(3): sum += array[i][j]
        if sum > max: 
            max = sum
            winners = 1
            coordinations = str(i)
        elif sum == max: 
            winners += 1
            coordinations += f", {i}"

    return f"{winners} | {coordinations}"

def multiplicationTable(size, result = ""):
    print("Завдання 23:\n", end='')

    array1 = []
    for i in range(size): # створення таблиці множення
        array2 = []
        for j in range(size): array2.append(i * j)
        array1.append(array2)
    
    for i in array1: # пеереведення масиву в стрінг
        for j in i: result += f"{j} "
        result += "\n"
    
    return result

def pascalTriangle(size, result = ""):
    print("Завдання 24:\n", end='')

    array1 = []
    for i in range(size):
        array2 = []
        for j in range(size):
            if j == 0 or i == 0: array2.append('1')
            else: array2.append('0')
        array1.append(array2)

    for i in range(size):
        for j in range(size):
            if j != 0 and i != 0: array1[i][j] = f"{int(array1[i-1][j]) + int(array1[i][j-1])}"

    for i in array1:
        for j in i: result += f"{j} "
        result += "\n"

    return result

def snake(n, m, result = ""):
    print("Завдання 26:\n", end='')

    array1 = []; num = 0
    for i in range(n):
        array2 = []
        for j in range(m):
            array2.append(num)
            num += 1
        if i % 2 != 0: array2.reverse()
        array1.append(array2)

    for i in array1:
        for j in i: result += f"{j} "
        result += "\n"

    return result


def sapper(day):
    if day > 0 and day <= 365:
        




if __name__ == "__main__":
    import main
    print("\n| Модулі\n")
    main.ARRAYS()