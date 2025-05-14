arr=list(map(int,input("enter the elements: ").split()))

l=arr[0]
for a in arr:
    if(a>l):
        l=a
    else:
        continue
print(l)