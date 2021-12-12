'''
349. Intersection of Two Arrays
'''
import time

nums1 = [1,2,2,1]
nums2= [2,2]

def bruteForce(nums1, nums2):
    res = set()
    for i in nums1:
        for j in nums2:
            if i==j:
                res.add(j)
    return res

def twoPointer(nums1, nums2):
    res = set()
    nums1.sort()
    nums2.sort()
    i = j = 0
    while i<len(nums1) and j<len(nums2):
        if nums1[i] < nums2[j]:
            i+=1
        elif nums1[i] > nums2[j]:
            j+=1
        else:
            res.add(nums1[i])
            i+=1
            j+=1
    return res

ans = twoPointer(nums1, nums2)
print(ans)