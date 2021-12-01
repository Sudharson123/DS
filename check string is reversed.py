def check(str1, str2):
    print(str1, str2)
    temp1 = ''
    print(len(str1), len(str2))
    if len(str1) == len(str2):
        a = len(str1) // 2
        for j in range(a, len(str1)):
            temp1 = temp1 + str1[j]
        for i in range(a):
            temp1 = temp1 + str1[i]
    print(temp1)
    if temp1 == str2:
        return True
    else:
        return False
