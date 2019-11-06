import math

t = int(input())

while(t>0):
    size = int(input())
    prod = list(map(int,input().split()))
    orig = []
    
    
    root = (1 + round(math.sqrt(8*size))) // 2

    v = round(math.sqrt((prod[0] * prod[1]) // prod[root-1]))

    orig.append(v)

    for i in range(root-1):
        orig.append(prod[i]//v)
            
    for o in orig:
        print(o,end = ' ')
    print()
    t -= 1
