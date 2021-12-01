def summ(a,sum_):
    count = 0
    result = []
    for i in range(0, len(a)):
        for b in range(i + 1, len(a)):
            if a[i] + a[b] == sum_:
                count += 1
                d = result.append([a[i], a[b]])
            else:
                pass
    print(len(result))


summ([1,1,1,1],2)