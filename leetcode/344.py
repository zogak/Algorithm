'''
344. Reverse String
'''

input = ["h","e","l","l","o"]

left, right = 0, len(input)-1
while left < right:
    input[left], input[right] = input[right], input[left]
    left += 1
    right -= 1
print(input)