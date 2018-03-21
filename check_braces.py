'''
An algorithm to check if the brackets/parentheses are in balance.

'''

def check_braces(expr):
    if len(expr)%2!=0:
        return "NO"
    opening=set('([{')
    match=set([ ('(',')'), ('[',']'), ('{','}') ])
    stack=[]
    for char in expr:
        if char in opening:
            stack.append(char)
        else:
            if len(stack)==0:
                return "NO"
            lastOpen=stack.pop()
            if (lastOpen, char) not in match:
                return "NO"
    return "YES"


#test

print braces("([[]])") # ---> YES
print braces("[[]])") # ---> NO
