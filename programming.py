l = ["network" , "math" , "programming" ,"music" , "physic"]
x=0
y=4
for i in range (0,len(l)):
    if len(l[x])>= len(l[y]):
        if len(l[x])>= len(l[y-1]):
            if len(l[x])>= len(l[y-2]):
                if len(l[x])>= len(l[y-3]):
                    if len(l[x])>= len(l[y-4]):
                        print(l[x])
    x=x+1
