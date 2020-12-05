#data harga buah
buah={'apel':5000,
      'jeruk':8500,
      'mangga':7800,
      'duku':6500}
i=0
hrg=[]

while True:
    beli=str(input('Nama buah yang dibeli   : '))
    bnyk=int(input('Berapa kg               : '))
    print()
    
    if beli in buah:
        if beli=='apel':
            total=5000*bnyk
            hrg.append(total)
            i+=1
        if beli=='jeruk':
            total=8500*bnyk
            hrg.append(total)
            i+=1
        if beli=='mangga':
            total=7800*bnyk
            hrg.append(total)
            i+=1
        if beli=='duku':
            total=6500*bnyk
            hrg.append(total)
            i+=1
    jwb=str(input('Beli buah yang lain (y/n)? '))
    
    while jwb=='y':
        print()
        beli=str(input('Nama buah yang dibeli   : '))
        bnyk=int(input('Berapa kg               : '))
        print()
        if beli in buah:
            if beli=='apel':
                total=5000*bnyk
                hrg.append(total)
                i+=1
            if beli=='jeruk':
                total=8500*bnyk
                hrg.append(total)
                i+=1
            if beli=='mangga':
                total=7800*bnyk
                hrg.append(total)
                i+=1
            if beli=='duku':
                total=6500*bnyk
                hrg.append(total)
                i+=1
        jwb=str(input('Beli buah yang lain (y/n)? '))
        
    if jwb=='n':
        sum=0
        for x in hrg:
            sum =sum+x
        tottal= sum
        print('-------------------------------------')
        print('Total harga              : Rp ',tottal)
        break
