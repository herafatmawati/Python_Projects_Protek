#funtion diffdate menghitung selisih tanggal hari ini dengan tanggal x

from datetime import*
def diffDate(x):
    y=x.split('-')
    tgl1=date(year=int(y[0]),month=int(y[1]),day=int(y[2]))
    tgl2=datetime.date(datetime.now())
    slsh=tgl1-tgl2
    print(slsh.days)
    return slsh
diffDate('2021-1-4')

