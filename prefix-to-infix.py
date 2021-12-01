def operators(x):
    if x=='/':
        return True
    elif x=='+':
        return True
    elif x=='-':
        return True
    elif x=='*':
        return True
    else:
        return False
def post_to_pre(str_):
    str1=str_[::-1]
    s=[]
    for i in range(len(str1)):
        if operators(str1[i])==False:
            s.append(str1[i])
        else:
            op1=s.pop(-1)
            op2=s.pop(-1)
            final="("+str(op1)+str1[i]+str(op2)+")"
            s.append(final)
    return final
x=post_to_pre('*+AB-CD')
print(x)