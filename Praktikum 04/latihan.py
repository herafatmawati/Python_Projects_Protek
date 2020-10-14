#latihan 1
tarif1=200000
tarif2=10000
jammulai=6
menitmulai=0
jamselesai=23
menitselesai=50
lamasewa=(jamselesai-jammulai)+((menitselesai-menitmulai)//60)
sewa1=1
sewa2=lamasewa-12
totaltarif=sewa1*tarif1 + sewa2*tarif2
print("total tarif sewa = Rp ",totaltarif, ",00")
print("---------------01--------------------")

#latihan 2
jarak=795
bbm=12
liter=jarak/bbm
print("Pak Budi perlu mengisi ",liter, "liter untuk perjalanan tersebut")
print("---------------02--------------------")

#latihan 3
isibensin=liter//50
print("Pak Budi harus mengisi bensin minimal ",isibensin,"kali")
print("---------------03--------------------")

#latihan 4
jarakAB=125
V1=62
jarakBC=256
V2=70
berangkat=6
rehat=45/60
waktu1=jarakAB//V1 
waktu2=jarakBC//V2 
waktutotal=(waktu1+waktu2)
sampai=berangkat+waktutotal
print("Pak Amir akan tiba pada pukul ",sampai,".00")
print("---------------04--------------------")

#latihan 5
laki=int(input("Jumlah mahasiswa laki- laki ="))
pr=int(input("Jumlah mahasiswa perempuan  ="))
jmlhlk='#'*laki
jmlhpr='#'*pr
print("Laki- laki : ",jmlhlk)
print("Perempuan  : ",jmlhpr)
print("---------------05--------------------")
