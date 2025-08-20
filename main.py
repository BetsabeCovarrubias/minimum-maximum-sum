result = float('inf')

def solveMinMaxSum(theNums, j, subNums):
    global result
    if j == (len(theNums)):
        result = min(result, max(subNums))
        return
    
    for i in range(len(subNums)):
        subNums[i] += theNums[j]
        if subNums[i] < result:
            solveMinMaxSum(theNums, j + 1, subNums)
        subNums[i] -= theNums[j]


if __name__ == '__main__':
    values = input().split()
    amountNums = int(values[0])
    groups = int(values[1])

    theNums = [-1] * amountNums
    before = input().split()
    for i, iSt in enumerate(before):
        theNums[i] = int(iSt)

    subNums = [0] * groups
    solveMinMaxSum(theNums, 0, subNums)
    print(result)