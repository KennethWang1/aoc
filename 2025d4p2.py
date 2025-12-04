dir = [[1,1],[0,1],[1,0],[1,-1],[-1,1],[-1,0],[0,-1],[-1,-1]]
arr = []
s = 0
x = 'placeholder'
while (x := input()) != 'X':
    arr.append(x)

update = False
while not update:
    update = True
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            ss = 0
            if arr[i][j] == '.':
                continue
            for item in dir:
                ni = i + item[0]
                nj = j + item[1]
                if 0 <= ni < len(arr) and 0 <= nj < len(arr[0]) and arr[ni][nj] == '@':
                    ss += 1
            if ss < 4:
                update = False
                arr[i] = arr[i][:j]+'.'+arr[i][j+1:]
                s += 1
print(s)
