def solution(commands):
    answer = []
    graph = [['']*51 for _ in range(51)]
    check = [[0]*51 for _ in range(51)]
    flag = 0

    for command in commands:
        if command[:2] == 'UP': #이 부분 어떻게 단어로 구분할지?
            # update 1 3 apple
            if command[7].isdigit():
                com, r, c, value = command.split() #이렇게 split 중 몇 개만 int로 바꾸어주고 싶을 땐 어떻게..?
                r, c = int(r), int(c)
                graph[r][c] = value
                for i in range(1, 51):
                    for j in range(1, 51):
                        if check[i][j]!=0 and (check[i][j] == check[r][c]):
                            graph[i][j] = value
            # update apple banana
            else:
                com, origin, value = command.split()
                for i in range(1, 51):
                    for j in range(1, 51):
                        if graph[i][j] == origin:
                            graph[i][j] = value

        
        elif command[:2] == 'ME':
            com, r1, c1, r2, c2 = command.split()
            r1, c1, r2, c2 = int(r1), int(c1), int(r2), int(c2)
            # 두 칸이 같을 때 (모두 값이 없거나 값이 같거나)
            if graph[r1][c1] == graph[r2][c2]:
                pass
            # 두 칸이 모두 값을 가지고 있을 때 (그 값이 서로 다름)
            # r1 c1으로 병합이 되었음
            elif graph[r1][c1]!='' and graph[r2][c2]!='':
                graph[r2][c2] = graph[r1][c1]

                if check[r1][c1] == 0:
                    flag += 1
                    check[r1][c1] = check[r2][c2] = flag
                else:
                    check[r2][c2] = check[r1][c1]
            
            # 둘 중 하나만 값을 가지고 있을 때
            else:
                # r1 c1으로 병합
                if graph[r1][c1] != '':
                    graph[r2][c2] = graph[r1][c1]

                    if check[r1][c1] == 0:
                        flag += 1
                        check[r1][c1] = check[r2][c2] = flag
                    else:
                        check[r2][c2] = check[r1][c1]

                # r2 c2로 병합
                elif graph[r2][c2] != '':
                    graph[r1][c1] = graph[r2][c2]

                    if check[r2][c2] == 0:
                        flag += 1
                        check[r2][c2] = check[r1][c1] = flag
                    else:
                        check[r1][c1] = check[r2][c2]


        elif command[:2] == 'UN':
            com, r, c = command.split()
            r, c = int(r), int(c)
            cells = []
            for i in range(1, 51):
                for j in range(1, 51):
                    if check[i][j] == check[r][c]:
                        cells.append((i,j))
                        check[i][j] = 0

            for cell in cells:
                if cell[0] == r and cell[1] == c:
                    continue
                else:
                    graph[cell[0]][cell[1]] = ''
        
        elif command[:2] == 'PR':
            com, r, c = command.split()
            r, c = int(r), int(c)
            if graph[r][c] == '':
                answer.append('EMPTY')
            else:
                answer.append(graph[r][c])
    
    print(graph)
    return answer

#print(solution(["UPDATE 1 1 menu", "UPDATE 1 2 category", "UPDATE 2 1 bibimbap", "UPDATE 2 2 korean", "UPDATE 2 3 rice", "UPDATE 3 1 ramyeon", "UPDATE 3 2 korean", "UPDATE 3 3 noodle", "UPDATE 3 4 instant", "UPDATE 4 1 pasta", "UPDATE 4 2 italian", "UPDATE 4 3 noodle", "MERGE 1 2 1 3", "MERGE 1 3 1 4", "UPDATE korean hansik", "UPDATE 1 3 group"]))
print(solution(["UPDATE 1 1 menu", "UPDATE 1 2 category", "UPDATE 2 1 bibimbap", "UPDATE 2 2 korean", "UPDATE 2 3 rice", "UPDATE 3 1 ramyeon", "UPDATE 3 2 korean", "UPDATE 3 3 noodle", "UPDATE 3 4 instant", "UPDATE 4 1 pasta", "UPDATE 4 2 italian", "UPDATE 4 3 noodle", "MERGE 1 2 1 3", "MERGE 1 3 1 4", "UPDATE korean hansik", "UPDATE 1 3 group", "UNMERGE 1 4", "PRINT 1 3", "PRINT 1 4"]))
#print(solution(["UPDATE 1 1 a", "UPDATE 1 2 b", "UPDATE 2 1 c", "UPDATE 2 2 d", "MERGE 1 1 1 2", "MERGE 2 2 2 1", "MERGE 2 1 1 1", "PRINT 1 1", "UNMERGE 2 2", "PRINT 1 1"]))
