def dataStat(x):
    sum=0
    l=0
    for angka in x:
        sum += angka
        l += 1
    mean= sum//l
    b=max(x)
    c=min(x)
    balikx=[mean,b,c]
    print(balikx)
    return balikx
    
x=[1,2,3,4,5]
dataStat(x)
