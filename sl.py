arr=list(map(int,input("enter the elements: ").split()))

l=arr[0]
sl=0

for a in arr:
    if(l<a):
        sl=l
        l=a
    else:
        continue
print(sl)