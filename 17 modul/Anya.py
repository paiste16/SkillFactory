
#программа, которую мне в помощь написала Аня Агабекян, но у меня искренне не хватило мозгов ее даже переработать(((
def get_input():
    array = []
    while array == []:
        temp = input("Введите последовательность чисел: ").split(' ')
        for a in temp:
            if a == '':
                continue
            try:
                x = int(a)
                array.append(x)
                idx = len(array)-1
                while idx > 0 and array[idx-1] > x:
                    array[idx] = array[idx-1]
                    idx -= 1
                array[idx] = x
            except ValueError:
                print("Требуется ввести числа!")
                array = []
                break
    return array

def lin_search(array, element):
    idx = len(array)-1
    while element <= array[idx]:
        idx -= 1
    return idx

array = get_input()
print(f"Отсортированная последовательность: {array}")
while True:
    try:
        element = int(input("Введите число: "))
        break
    except ValueError:
        print("Требуется ввести число!")

idx = lin_search(array, element)
print(f"\nНомер позиции элемента: {idx},")
print(f"Который меньше введенного числа: {element},")
print(f"А следующий за ним больше или равен этому числу: {'Элемент больше всех в последовательности' if idx == len(array)-1 else str(array[idx+1])},")
print(f"Значение этого элемента {array[idx]}.")