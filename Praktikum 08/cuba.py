nilaiMhs=[{'nim':'A01','nama':'Amir','mid':50,'uas':80},
          {'nim':'A02','nama':'Budi','mid':40,'uas':90},
          {'nim':'A03','nama':'Cici','mid':50,'uas':50},
          {'nim':'A04','nama':'Dedi','mid':20,'uas':30},
          {'nim':'A05','nama':'Fifi','mid':70,'uas':40}]
nilai=[]
na1=((nilaiMhs[0]['mid']+ 2*nilaiMhs[0]['uas']))//3
print(na1)
nilai.append(na1)
na2=((nilaiMhs[1]['mid']+ 2*nilaiMhs[1]['uas']))//3
print(na2)
nilai.append(na2)
na3=((nilaiMhs[2]['mid']+ 2*nilaiMhs[2]['uas']))/3
print(na3)
nilai.append(na3)
na4=((nilaiMhs[3]['mid']+ 2*nilaiMhs[3]['uas']))//3
print(na4)
nilai.append(na4)
na5=((nilaiMhs[4]['mid']+ 2*nilaiMhs[4]['uas']))//3
print(na5)
nilai.append(na5)
nilai.sort(reverse= True)
print(nilai[0])
nilaiMhs
