#program tampil data list ke bentuk tabel

nilai=[{'nim':'A01','nama':'Agustina','n.mid':50,'n.uas':80},
       {'nim':'A02','nama':'Budi','n.mid':40,'n.uas':90},
       {'nim':'A03','nama':'Chicha','n.mid':100,'n.uas':50},
       {'nim':'A04','nama':'Donna','n.mid':20,'n.uas':100},
       {'nim':'A05','nama':'Fatimah','n.mid':70,'n.uas':100}]

print('='*60)
for i in nilai[0].keys():
    print(i.upper(),end='\t\t')  
print()
print('-'*60)
x='A01\t\tAgustina'.upper()
print(x,str(50).center(22),str(80).center(7))
y='A02\t\tBudi'.upper()
print(y,str(40).rjust(16),str(90).rjust(15))
z='A03\t\tChicha'.upper()
print(z,str(100).rjust(14),str(50).rjust(15))
a='A04\t\tDOnna'.upper()
print(a,str(20).rjust(15),str(100).rjust(15))
b='A04\t\tFatimah'.upper()
print(b,str(70).rjust(13),str(100).rjust(15))
print('-'*60)
