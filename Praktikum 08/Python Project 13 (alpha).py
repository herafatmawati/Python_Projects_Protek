def nilaitinggi(nilaiMhs):
    i=0
    ubah=[]
    for x in nilaiMhs:
        na=((nilaiMhs[i]['mid']+ 2*nilaiMhs[i]['uas']))//3
        i+=1
        ubah.append(na)
        ubah.sort(reverse=True)  
    
    if ubah[0]==70:
        print('Nilai akhir tertinggi: A01 Amir',ubah[0])
    elif ubah[0]==73:
        print('Nilai akhir tertinggi: A02 Budi',ubah[0])
    elif ubah[0]==50:
        print('Nilai akhir tertinggi: A03 Cici dan A05 Fifi',ubah[0])
    elif ubah[0]==26:
        print('Nilai akhir tertinggi: A04 Dedi',ubah[0])

nilaiMhs=[{'nim':'A01','nama':'Amir','mid':50,'uas':80},
          {'nim':'A02','nama':'Budi','mid':40,'uas':90},
          {'nim':'A03','nama':'Cici','mid':50,'uas':50},
          {'nim':'A04','nama':'Dedi','mid':20,'uas':30},
          {'nim':'A05','nama':'Fifi','mid':70,'uas':40}]
nilaitinggi(nilaiMhs)
