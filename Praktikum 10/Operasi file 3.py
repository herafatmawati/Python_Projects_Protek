#program membaca file datamahasiswa.txt
#ubah ke dictonary

output=[]
dataMhs={}
fileku=open('d:\datamahasiswa.txt','r')
konten=fileku.read().splitlines()

for line in konten:
    a=line.split('|')
    dataMhs={'nim':a[0],'nama':a[1],'alamat':a[2]}
    output.append(dataMhs)
print(output)

fileku.close()
