#!/usr/bin/env python3

def zeroMatrix(arr):
    zero_out = []
    for i in range(0,len(arr)):
        for j in range(0,len(arr[0])):
            if arr[i][j] == 0:
                zero_out.append([i,j])
    for pos in zero_out:
        arr[pos[0]] = [0] * len(arr[0])
        for num in [x for x in range(0,len(arr))]:
            arr[num][pos[1]] = 0
    return arr


zeroMatrix([[1,0,1],[1,1,1]])
zeroMatrix([[1,0,1],[0,1,1]])
zeroMatrix([[1,0,1,1],[0,1,1,3],[1,1,1,1]])
