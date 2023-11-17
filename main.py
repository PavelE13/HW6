from Search.BinarySearch import BinarySearch

arr = [1, 3, 5, 7, 9, 11, 13, 15, 17] # arr (list): Массив, в котором будет производиться поиск.
target = 3 # цель поиска.
binary_search = BinarySearch(arr) #Создание объекта класса BinarySearch с массивом arr
result = binary_search.search(target) #Поиск целевого элемента в массиве arr
print(f'индекс элемента {target} в массиве {arr} равен {result}') #Вывод результата поиска (индекс элемента 9 в массиве arr)
