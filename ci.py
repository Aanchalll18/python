p,r,t=map(int,input("enter principal rate and time ").split())

amt=p*((1+r/100)**t)
res=amt-p
print(res)