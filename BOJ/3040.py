hats = []
for _ in range(9):
    hats.append(int(input()))

hats.sort()
sumOfTwoFakes = sum(hats) - 100

left, right = 0, 8
while left < right:
    if hats[left] + hats[right] < sumOfTwoFakes:
        left += 1
    elif hats[left] + hats[right] > sumOfTwoFakes:
        right -= 1
    elif hats[left] + hats[right] == sumOfTwoFakes:
        break

for i in range(9):
    if i==left or i==right: continue
    print(hats[i])