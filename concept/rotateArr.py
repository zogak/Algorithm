arr = [1,2,3,4,5,6,7]

def rotate(arr, n):
    length = len(arr)
    res = [0]*length
    
    for i in range(length):
        res[(i+n)%length] = arr[i]
        
    return res

res = rotate(arr, 2)
print(res)