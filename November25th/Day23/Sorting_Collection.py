import random
arr = []
while len(arr)<20:
    arr.append(random.randrange(1, 100))

print(arr)

def bubble_sort(list_test):
    for i in len(list_test):
        for j in (len(list_test)-i-1):
            if list_test[j] < list_test[j+1]:
                list_test[j] , list_test[j+1] = list_test[j+1] ,list_test[j]
            print(list_test)

bubble_sort(arr)
