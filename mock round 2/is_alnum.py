def alnum(n):
    if(n==''):
        return False
    for word in n:
        if not('a'<=word<='z' or 'A'<=n<='Z' or '0'<=word<='9' ):
            return False
        # elif ('A'<=n<='Z'):
        #     return True
        # elif(0<int(n)<9):
        #     return True
        # else:
        #     return True
    else:
        return True
    
# var=input("enter the value")
result=alnum("")
print(result)
    
    