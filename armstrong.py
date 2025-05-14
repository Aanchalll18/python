n=int(input("enter a number: "))
temp=n
digits=len(str(n))
res=0

while temp>0:
    digit=temp%10
    res+=digit**digits
    temp //=10
if(res==n):
    print(n,"is armgstrong")
else:
    print(n,"is not an armgstrong")

    
