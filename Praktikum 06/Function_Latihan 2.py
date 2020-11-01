n=int(input('Masukkan berapa banyak formasi bintang yang diinginkan: '))
def starFormation1(n):
    string= ""
    baris=1
    while baris<=n:
        kolom=baris
        while kolom>0:
            string=string+"*"
            kolom=kolom-1
        string=string+"\n"
        baris=baris+1
    print(string)

    
def starFormation2(n):
    string=""
    baris=n
    while baris>= 0:
        kolom=baris
        while kolom>0:
            string= string+"*"
            kolom=kolom-1
        string=string+"\n"
        baris=baris-1
    print(string)
    


starFormation1(n)
starFormation2(n)
    
