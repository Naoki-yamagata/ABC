
L,Q =map(int,input().split())
wood =[i+1 for i in range(L-1)]
wood.append(0)

for i in range(Q):
    c,x=map(int,input().split())
    
    if c == 1:
        wood[x-1] = 0

    if c == 2:
        cut =[i for i, x in enumerate(wood) if x == 0]
        d = 0
        for i in range(len(cut)-1):
            if cut[i]< x-1 <cut[i+1]:
                print(cut[i+1]-cut[i])
                d = 1
        if d == 0:
            print(wood.index(0)+1)

