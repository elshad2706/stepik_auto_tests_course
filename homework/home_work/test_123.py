list1 = [1,2,3,4]
def number(list):
    sets = set(list)
    if len(sets) < len(list):
        print("Есть дубль")
    else:
        print("Дублей нет")



number(list1)

list_1 = [1,3,2,10,43,210]
number = int()
for i in list_1:
    if i > number:
        number = i

print("максимальное число", number)