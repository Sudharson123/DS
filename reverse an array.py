def reverse(a):
    start=0
    end=len(a)-1
    while start<end:
        a[start],a[end]=a[end],a[start]
        start+=1
        end-=1
        continue
    print(a)


reverse([1,2,3,4,5,6,7,8,9,10,11])