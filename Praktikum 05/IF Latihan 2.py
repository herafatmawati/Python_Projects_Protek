#program Status Kelulusan
print('Status Kelulusan Ujian Mahasiswa')
print('')

bi=int(input("Masukkan Nilai Bahasa Indonesia : "))
mm=int(input("Masukkan Nilai Matematika       : "))
ipa=int(input("Masukkan Nilai IPA              : "))

print('')

if bi>=0 and bi<=100 and mm>=0 and mm<=100 and ipa>=0 and ipa<=100:
    if bi >=60 and mm>70 and ipa>=60:
        print('Status Kelulusan                : LULUS')
    elif bi<60 and mm<=70 and ipa<60:
        print('Status Kelulusan                : TIDAK LULUS')
else:
    print('Ada Nilai Input yang Tidak Valid')
