h, w = map(int, input().split())
height = list(map(int, input().split()))

ans = 0
left, right = 0, len(height)-1
left_max, right_max = height[left], height[right]

while left < right:
    left_max = max(left_max, height[left])
    right_max = max(right_max, height[right])

    if left_max <= right_max:
        ans += left_max - height[left]
        left += 1

    else:
        ans += right_max - height[right]
        right -= 1


print(ans)