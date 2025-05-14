n=int(input("enter a number"))

def fact(n):
    return 1 if (n==0 or n==1) else n*fact(n-1)
print(fact(n))

'''n = 6

# Initialize the factorial variable to 1
fact = 1

# Calculate the factorial using a for loop
for i in range(1, n + 1):
    fact *= i

print(fact)'''