def sum(*data):
    sum=0
    for angka in data:
        sum+=angka
    
def average(*data):
    sum=0
    l=0
    for angka in data:
        sum += angka
        l += 1
    mean= sum/l
    print('Rata-rata: ',mean)
    
   
def maks(*data):
    besar=0
    for angka in data:
        if angka> besar:
            besar=angka
    return besar
        
def min(*data):
    kecil=99
    for angka in data:
        if angka<kecil:
            kecil=angka
    return kecil
   
    
