switch = int(input())
status = [0] + list(map(int, input().split()))
studentNum = int(input())
students = []

def turn(n):
    if n==0:
        return 1
    else:
        return 0

for _ in range(studentNum):
    students.append(list(map(int, input().split())))

for student in students:
    gender, number = student
    
    if gender == 1:
        for i in range(1, len(status)):
            if i%number == 0:
                status[i] = turn(status[i])
    
    elif gender == 2:
        if number == 1 or number == len(status)-1:
            status[number] = turn(status[number])
        else:
            left, right = number, number
            while left >= 1 and right <= len(status)-1:
                left -= 1
                right += 1
                if status[left] != status[right]:
                    left += 1
                    right -= 1
                    break
            for i in range(left, right+1):
                status[i] = turn(status[i])

for i, s in enumerate(status):
    if i==0: continue
    print(s, end=' ')
    if i%20 == 0:
        print()
