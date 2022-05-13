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
                    


if __name__ == "__main__": 
    import main
    print("\n| Модулі\n")
    main.ARRAYS()