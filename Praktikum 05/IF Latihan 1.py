#program Status Kelulusan
print('Status Kelulusan Ujian Mahasiswa')
print('')

bi=int(input("Masukkan Nilai Bahasa Indonesia : "))
mm=int(input("Masukkan Nilai Matematika       : "))
ipa=int(input("Masukkan Nilai IPA              : "))

print('')

if bi >60 and ipa>60 and mm>70:
    print('Status Kelulusan                : LULUS')
else:
    print('Status Kelulusan                : TIDAK LULUS')
