#program replace huruf

def ubahHuruf(teks,a,b):
    ubah=teks.split()
    for t in teks:
        ubahhuruf=teks.replace(a,b)
    print(ubahhuruf)
    return ubahhuruf

ubahHuruf('MATEMATIKA','T','S')
ubahHuruf('HERA FATMAWATI','A','C')
