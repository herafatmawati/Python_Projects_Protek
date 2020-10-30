import random
def tebak():
    print('Holla.. saya Mr.acakadul ingin mengajakmu bermain tebak angka.')
    print('Saya sudah memilih angka acak antara 0 s/d 100. Kamu tebak ya!')
    print()
    start= 0
    end= 100
    skor=100
    
    answer=random.randint(1,100)
    useranswer=False
    i=1
    while True:
        print('Tebak angka antara ',str(start)+' sampai',str(end))
        useranswer=int(input('Tebakanmu: '))

        if useranswer>=0 and useranswer<=100:
            if useranswer>answer:
                end=useranswer
                print('Hehe, angka yang kamu pilih terlalu besar')
            elif useranswer<answer:
                start=useranswer
                print('Hehe, angka yang kamu pilih terlalu kecil')
            elif useranswer == answer:
                print('Yeay, kamu berhasil menebaknya. Awesome!')
                if i <= 4:
                    print('Kamu sangat beruntung hari ini!')
                break
        else:
            print('Hmm, masukkan angka tebakanmu dengan benar antara ',str(start)+' sampai',str(end))
            
        i=i+1
    print('Kamu menebak dalam ',str(i), ' percobaan')
    print('')
    skor=skor- 2*(i+1)+4
    print('Skor kamu : ',skor)
        
tebak()
