fname=input('Masukkan nama : ')
try:
    print('Isi file ',fname,'adalah: ')
    read=open(fname,'r')
    for i in read:
        print(i)
except:
    print('File yang diminta tidak ada')
