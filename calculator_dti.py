import re

result = input("enter expression: ")
aftersplit = re.split(r"([-+*/])", result)


while len(aftersplit) >1:
    for i in (aftersplit):
        if i in ['/', '*']:
            x = aftersplit.index(i)
            a = aftersplit[x-1]
            b = aftersplit[x+1]
            result = float(a)/float(b) 
            aftersplit[x] = result
            aftersplit.pop(x+1)
            aftersplit.pop(x-1)
    
    for i in (aftersplit):
        if i in ['*']:
            x = aftersplit.index(i)
            a = aftersplit[x-1]
            b = aftersplit[x+1]
            result = float(a)*float(b)
            aftersplit[x] = result
            aftersplit.pop(x+1)
            aftersplit.pop(x-1)
            
    
    for i in (aftersplit):
        if i in ['+','-']:
            x = aftersplit.index(i)
            a = aftersplit[x-1]
            b = aftersplit[x+1]
            result = float(a)+float(b) if i == '+' else float(a)-float(b)
            aftersplit[x] = result
            aftersplit.pop(x+1)
            aftersplit.pop(x-1)
    
print("Result: ", aftersplit[0])

        
