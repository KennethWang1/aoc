arr = []
op = []
s = 0
while True:
    i = input()
    x = i.split(' ')
    x = [_ for _ in x if _ != '']
    try:
        x = [int(_) for _ in x]
        arr.append(i)
    except:
        op = i.split(' ')
        op = [_ for _ in op if _ != '']
        break

count = 0
running = 0
x = 0
for j in range(len(arr[0])):
    for i in range(len(arr)):
        if(arr[i][j] == ' '):
            continue
        x = x * 10
        x += int(arr[i][j])
    if(x == 0):
        count += 1
        s += running
        running = 0;
        continue
    if running == 0:
        running = x
    else:
        exec("running=running"+op[count]+"x")
    x = 0
s += running

print(s)
