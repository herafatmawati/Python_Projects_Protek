#program pengacakan menggunakan function shuffleString(x,n)
def shuffleString(x,n):
    import random
    f=[]
    for i in range (n):
        y=f.append(''.join(random.sample(x,len(x))))
    print(f)

shuffleString('aku',2)
shuffleString('aku',3)        
shuffleString('aku',4)


