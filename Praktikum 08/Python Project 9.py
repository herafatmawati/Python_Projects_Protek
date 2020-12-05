#data harga buah
buah={'apel':5000,
      'jeruk':8500,
      'mangga':7800,
      'duku':6500}
buah2=list(buah)

while True:
    beli=str(input('Nama buah yang dibeli : '))
    bnyk=int(input('Berapa kg             : '))
    print('-------------------------------------')
    if beli=='':
        break

    if beli in buah2:
        if beli==buah2[0]:
            total=5000*bnyk
            print('Total harga           : Rp ',total)
            break
        if beli==buah2[1]:
            total=8500*bnyk
            print('Total harga           : Rp ',total)
            break
        if beli==buah2[2]:
            total=7800*bnyk
            print('Total harga           : RP ',total)
            break
        if beli==buah2[3]:
            total=6500*bnyk
            print('Total harga           : Rp ',total)
            break
