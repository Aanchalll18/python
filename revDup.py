a=list(map(int,input("enter the elements: ").split()))

s=set()
res=[]

for i in a:
    if i not in s:
        s.add(i)
        res.append(i)
print(res)

'''
a = list(map(int, input("Enter the elements: ").split()))
result = list(dict.fromkeys(a))
print("List after removing duplicates:", result)


'''