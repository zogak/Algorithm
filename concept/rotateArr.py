arr = [1,2,3,4,5,6,7,8,9]

def rotate(arr, n):
    length = len(arr)
    res = [0]*length
    
    for i in range(length):
        res[(i+n)%length] = arr[i]

    return res

print(rotate(arr, 2))

def reverse_the_reversed(arr, n):
    left, right = arr[:-2], arr[-2:]
    reversed_list = list(reversed(left)) + list(reversed(right))
    return list(reversed(reversed_list))

reverse_the_reversed(arr, 2)

def juggling(arr, n):
    length = len(arr)

    if length%n == 0:
        t = arr[0]
        for i in range(n):
            start = length-n+i
            T = arr[start]
            s = start

            while s-n >=0:
                arr[s] = arr[s-n]
                s -= n
            
            arr[i] = T
    return arr

print(juggling(arr, 3))

def getMaxSum(arr):
    ans = 0
    tmp = 0
    for i, value in enumerate(arr):
        tmp += i*value
    
    length = len(arr)
    for i in range(1, length):
        tmp = 0
        rotated_list = rotate(arr, i)
        for i, value in enumerate(rotated_list):
            tmp += i*value

            if tmp > ans:
                ans = tmp
    return ans

a = [10,1,2,3,4,5,6,7,8,9]
print(getMaxSum(a))

def makeIndexValueSame(arr):
    length = len(arr)
    for i in range(length):
        if arr[i] == -1 or arr[i] == i:
            continue
        