def result(s):
    g= 0
    ans=False
    for i in s:
        if i =="(":
            g += 1
        elif i ==")":
            g-= 1
        if g < 0:
            return ans
    if g==0:
        return not ans
    return ans
x=result("()(())")
print("paranthesis balancing is:",x)