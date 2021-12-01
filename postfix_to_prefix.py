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
    s=[]
    for i in range(len(str_)):
        if operators(str_[i])==False:
            s.append(str_[i])
        else:
            op1=s.pop(-1)
            op2=s.pop(-1)
            final=str_[i]+str(op2)+str(op1)
            s.append(final)
    return final
x=post_to_pre('ABC/-AK/L-*')
print(x)