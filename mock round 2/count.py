var=input("enter the string\n")
count=0
for word in var:
    if('A'<=word<='Z' or 'a'<=word<='z'):
        count+=1
print(count)
