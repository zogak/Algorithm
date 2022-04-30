def solution(numbers, hand):
    answer = ''
    location = {
        '1' : [0,0],
        '2' : [0,1],
        '3' : [0,2],
        '4' : [1,0],
        '5' : [1,1],
        '6' : [1,2],
        '7' : [2,0],
        '8' : [2,1],
        '9' : [2,2],
        '*' : [3,0],
        '0' : [3,1],
        '#' : [3,2]
    }
    
    num_in_left = [1, 4, 7]
    num_in_right = [3, 6, 9]
    #num_in_mid = [2, 5, 8, 0]
    
    cur_left = "*"
    cur_right = "#"
    
    for num in numbers:
        if num in num_in_left:
            answer+="L"
            cur_left = num
        elif num in num_in_right:
            answer+="R"
            cur_right = num
        else:
            num_location = location[str(num)]
            left_location = location[str(cur_left)]
            right_location = location[str(cur_right)]
            
            #print('num_loc {}, left_loc {}, right_loc {}'.format(num_location, left_location, right_location))
            left_dist = abs(num_location[0]-left_location[0]) + abs(num_location[1]-left_location[1])
            
            right_dist = abs(num_location[0]-right_location[0]) + abs(num_location[1]-right_location[1])
            
            #print('dist', left_dist, right_dist)

            if left_dist < right_dist:
                cur_left = num
                answer+="L"
            elif left_dist > right_dist:
                cur_right = num
                answer+="R"
            else:
                #print("same distance")
                if hand=="right":
                    cur_right = num
                    answer+="R"
                else:
                    cur_left = num
                    answer+="L"
            #print("answer", answer)
    return answer

numbers = [1,3,4,5,8,2,1,4,5,9,5]
hand = "right"
print(solution(numbers, hand))