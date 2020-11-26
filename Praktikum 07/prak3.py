file=open("d:/data1.txt","r")
try:
    sum=0
    for data1 in file:
        sum=sum+int(data1)
    print(sum)
except ValueError:
    print('Invalid Value')
