'''
각 자릿수의 합 구하기
'''

#1
target = 123
tmp = str(target)
ans = 0
for t in tmp:
    ans += int(t)

print(ans)

#2
target = 234
ans = 0
while True:
    moc = target // 10
    r = target % 10
    ans += r

    target = moc
    if moc == 0:
        break
print(ans)

# 2를 리팩토링하면
target = 345
ans = 0
while target > 0:
    ans += target % 10
    target = target // 10
print(ans)