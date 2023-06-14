def solution(rc, operations):
    n, m = len(rc), len(rc[0])
    def shift():
        nonlocal rc
        rc = [rc[-1]]+rc[:-1]

    def rotate():
        nonlocal rc
        temp = rc[0][0]
        for i in range(n-1):
            rc[i][0] = rc[i+1][0]
        for i in range(m-1):
            rc[n-1][i] = rc[n-1][i+1]
        for i in range(n-1, 0, -1):
            rc[i][m-1] = rc[i-1][m-1]
        for i in range(m-1, 0, -1):
            rc[0][i] = rc[0][i-1]
        
        rc[0][1] = temp
    
    for operation in operations:
        if operation == "Rotate":
            rotate()
            print(rc)
        elif operation == "ShiftRow":
            shift()
            print(rc)
    return rc

rc = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
operations = ["Rotate", "ShiftRow"]

solution(rc, operations)