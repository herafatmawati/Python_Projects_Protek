print('=================6=================')
#program menghitung luas segitiga function
#alas 10 satuan dan tinggi 20 satuan
def luasSegitiga(a,t):
    luas = a * t / 2
    return luas

alas = 10
tinggi = 20
print('Luas segitigas dg alas ',alas,
      ' dan tinggi ',tinggi,
      ' adalah ', luasSegitiga(alas,tinggi))
alas = 15
tinggi = 45
print('Luas segitigas dg alas ',alas,
      ' dan tinggi ',tinggi,
      ' adalah ', luasSegitiga(alas,tinggi))

print('=================7=================')
#program menghitung luas segitiga2 function
#alas 10 satuan dan tinggi 20 satuan
#nomor2
def luasSegitiga2(a,t):
    luas = a * t / 2
    print('Luas segitiga dg alas ',a,
          ' dan tinggi ',t,
          ' adalah ',luas)
    
alas = 10
tinggi = 20
luasSegitiga2(alas,tinggi)

alas = 15
tinggi = 45
luasSegitiga2(alas,tinggi)
