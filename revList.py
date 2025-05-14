a=input("enter the elements").split()
s,e=0,len(a)-1

while s<e:
    a[s],a[e]=a[e],a[s]
    s+=1
    e-=1
print(a)