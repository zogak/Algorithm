#bubble sort
def bubble_sort(my_list):
    for i in range(len(my_list)-1, 0, -1):
        for j in range(i):
            if my_list[j] > my_list[j+1]:
                my_list[j], my_list[j+1] = my_list[j+1], my_list[j]
    return my_list

print(bubble_sort([4, 2, 6, 5, 1, 3]))

#selection sort
def selection_sort(my_list):
    for i in range(len(my_list)-1):
        min_index = i
        for j in range(i+1, len(my_list)):
            if my_list[j] < my_list[min_index]:
                min_index = j
        if i != min_index:
            temp = my_list[i]
            my_list[i] = my_list[min_index]
            my_list[min_index] = temp
    return my_list

print(selection_sort([4, 2, 6, 5, 1, 3]))

#insertion sort
def insertion_sort(my_list):
    for i in range(1, len(my_list)):
        temp = my_list[i]
        j = i-1
        while temp < my_list[j] and j > -1:
            my_list[j+1] = my_list[j]
            my_list[j] = temp
            j -= 1

#merge sort
def mergeLR(x, y):
    res = []
    i, j = 0, 0
    while i < len(x) and j < len(y):
        if x[i] < y[j]:
            res.append(x[i])
            i += 1
        else:
            res.append(y[j])
            j += 1
        
    if i == len(x):
        while j < len(y):
            res.append(y[j])
            j += 1

    if j == len(y):
        while i < len(x):
            res.append(x[i])
            i += 1

    return res

def mergeSort(x):
    if len(x) <= 1:
        return x
    
    mid = len(x)//2
    left = mergeSort(x[:mid])
    right = mergeSort(x[mid:])

    res = mergeLR(left, right)
    return res
