s = 0

def rawr(x, string, term, start):
    global s
    l = 0
    loc = 0
    
    #print(string)
    for i in range(len(string)):
        smth = int(string[i])
        if(smth > l):
            l = smth
            loc = i
    s = s + l * pow(10, term-1)
    #print(loc)
    if(term != 1):
        rawr(x, x[(loc + start + 1):(len(x)-term + 2)], term - 1,loc + start+1)
    return

while ((x:=input()) != 'X'):
    rawr(x, x[0:len(x)-11], 12,0)
    
    
print(s)
