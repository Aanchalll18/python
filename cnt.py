a=list(map(int,input("enter the numbers: ").split()))
dit={}

for i in a:
    if i not in dit:
        dit[i] = 1
    else:
        dit[i] +=1
print(dit)

for dup in dit:
    if(dit[dup] > 1):
        print(dup)
