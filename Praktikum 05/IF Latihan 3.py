#program Status Kelulusan
print('Status Kelulusan Ujian Mahasiswa')
print('')

bi=int(input("Masukkan Nilai Bahasa Indonesia : "))
mm=int(input("Masukkan Nilai Matematika       : "))
ipa=int(input("Masukkan Nilai IPA              : "))
print('')

if bi >=60 and bi<=100 and mm>70 and mm<=100 and ipa>=60 and ipa<=100:
    print('Status Kelulusan                : LULUS')
elif bi >=0 and bi<60 or mm>=0 and mm<=70 or ipa>=0 and ipa<60:
    print('Status Kelulusan                : TIDAK LULUS')
    print('Sebab')
    if bi>=0 and bi<60 :
        print('- Nilai Bahasa Indonesia kurang dari 60')
    if mm>=0 and mm<=70 :
        print('- Nilai Matetimatika kurang dari 70')
    if ipa>=0 and ipa<60 :
        print('- Nilai IPA kurang dari 60')
else:
    print('Ada Nilai Input yang Tidak Valid')
