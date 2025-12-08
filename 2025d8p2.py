import math
arr = []
dsu = []
x = ""
cc = 0
while (x:= input()) != "":
    if (x == "X"):
        break
    x = x.split(',')
    arr.append([int(_) for _ in x])
    dsu.append(cc)
    cc += 1
#arr.sort()
dist = [[(float('inf'),0,0) for __ in range(len(arr))] for _ in range(len(arr))]
for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if i == j:
                continue
            dist[i][j] = ((arr[i][0]-arr[j][0])**2+(arr[i][1]-arr[j][1])**2+(arr[i][2]-arr[j][2])**2,i,j)

dist = [i for s in dist for i in s]
#print(dist)
dist.sort()

smth = 0
total = 0
while (len(set(dsu)) > 1):
    i1 = dist[smth][1]
    i2 = dist[smth][2]
    total = arr[i1][0] * arr[i2][0] 
    minIndex = min(dsu[i1], dsu[i2])
    i1 = dsu[i1]
    i2 = dsu[i2]
    for k in range(len(dsu)):
        if dsu[k] == i1 or dsu[k] == i2:
            dsu[k] = minIndex
    smth += 1


print(total)
