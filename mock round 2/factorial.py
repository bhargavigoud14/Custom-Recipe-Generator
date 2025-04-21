def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    return fact

# n=int(input())
l=[]
for i in range(1,16):
    sum=factorial(i)
    l.append(sum)
    # print(sum)
print(l)
print(l[0]+l[-1])
