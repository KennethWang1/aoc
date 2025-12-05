arr = []
x = 'bleh'

count = 0

while (x:=input()) != 'X':
    list = x.split('-')
    list[0] = int(list[0])
    list[1] = int(list[1])
    for i in arr:
        if list[0] >= i[0] and list[0] <= i[1]:
            list[0] = i[1]+1
            i[1] = max(list[1],i[1])
        if list[0] > list[1]:
            break 
        if list[1] <= i[1] and list[1] >= i[0]:
            i[0] = min(list[0],i[0])
            list[1] = i[0]-1
    if(list[0] <= list[1]):
        arr.append([int(list[0]),int(list[1])])

for i in arr:
    for j in arr:
        if(i == j):
            continue
        if j[0] >= i[0] and j[0] <= i[1]:
            i[1] = max(j[1],i[1])
            arr.remove(j)
            continue
        if j[1] <= i[1] and j[1] >= i[0]:
            i[0] = min(j[0],i[0])
            arr.remove(j)
for i in arr:
    count += int(i[1])-int(i[0])+1
#print(arr)
print(count)
