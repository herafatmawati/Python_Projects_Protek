#program tampil data list ke bentuk tabel

nilai=[{'nim':'A01','nama':'Agustina','n.mid':50,'n.uas':80,'n.akhir':70,'status':'LULUS'},
       {'nim':'A02','nama':'Budi','n.mid':40,'n.uas':90,'n.akhir':73,'status':'LULUS'},
       {'nim':'A03','nama':'Chicha','n.mid':100,'n.uas':50,'n.akhir':66,'status':'LULUS'},
       {'nim':'A04','nama':'Donna','n.mid':20,'n.uas':100,'n.akhir':73,'status':'LULUS'},
       {'nim':'A05','nama':'Fatimah','n.mid':70,'n.uas':100,'n.akhir':90,'status':'LULUS'}]

na=(nilai[0]['n.mid']+2*nilai[0]['n.uas'])//3
if na >=60:
    status='LULUS'
else:
    status='TIDAK LULUS'
na1=(nilai[1]['n.mid']+2*nilai[1]['n.uas'])//3
if na1 >=60:
    status='LULUS'
else:
    status='TIDAK LULUS'
na2=(nilai[2]['n.mid']+2*nilai[2]['n.uas'])//3
if na2 >=60:
    status='LULUS'
else:
    status='TIDAK LULUS'
na3=(nilai[3]['n.mid']+2*nilai[3]['n.uas'])//3
if na3 >=60:
    status='LULUS'
else:
    status='TIDAK LULUS'
na4=(nilai[4]['n.mid']+2*nilai[4]['n.uas'])//3
if na4 >=60:
    status='LULUS'
else:
    status='TIDAK LULUS'

print('='*67)
for i in nilai[0].keys():
    print(i.upper().ljust(12),end='')
    
print()
print('-'*67)

print('A01','Agustina'.upper().rjust(16),str(50).rjust(8),str(80).rjust(10),str(70).rjust(13),'LULUS'.rjust(11))
print('A02','Budi'.upper().center(20),str(40).rjust(4),str(90).rjust(10),str(73).rjust(13),'LULUS'.rjust(11))
print('A03','Chicha'.upper().center(21),str(100).rjust(0),str(50).rjust(10),str(66).rjust(13),'LULUS'.rjust(11))
print('A04','DOnna'.upper().center(21),str(20).rjust(3),str(100).rjust(10),str(73).rjust(13),'LULUS'.rjust(11))
print('A05','Fatimah'.upper().rjust(15),str(70).rjust(9),str(100).rjust(10),str(90).rjust(13),'LULUS'.rjust(11))
print('-'*67)
