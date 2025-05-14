a=list(map(int,input("enter the elements").split()))

res=list(filter(lambda x: x % 2 == 0,a))
print (res)