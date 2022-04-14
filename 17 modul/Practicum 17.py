#то что я по честному реализовал сам, плохо конечно и не правильно, но как умел, не успеваю сделать лучше к сожалению(((
array = list(map(int, input("Введите много циферок через пробел(Только не больше десяти, а то работать не будет)))):").split()))
element = int(input("Введиде циферку которую ищем:"))

for i in range(len(array)):
    for j in range(len(array) - i - 1):
        if array[j] > array[j + 1]:
            array[j], array[j + 1] = array[j + 1], array[j]

def binary_search(array, element, left, right):
    if left > right:
        return False

    middle = (right + left) // 2
    if array[middle] == element:
        return middle
    elif element < array[middle]:
        return binary_search(array, element, left, middle - 1)
    else:
        return binary_search(array, element, middle + 1, right)




print(f"Такая вот отсортированная последовательность у нас получилась:{array}")
print(f"Номер элемента в массиве, который искали: {binary_search(array, element, array[1], array[-1])}")
x = (array[(binary_search(array, element, array[1], array[-1]) - 1)])
if x < element:
    print(f"номер элемента массива, который находится левее запрошенного числа и меньше него, а следкющий за ним больше или равен запрошенному числу {binary_search(array, element, array[1], array[-1]) - 1}")
else:
    print("Нет элементов удовлетворяющих условиям")