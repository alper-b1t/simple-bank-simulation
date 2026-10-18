import config
import getpass

def bank(budget):
    operation = 1
    while operation != 4:
        print("Hosgeldiniz,yapmak istediginiz islemi secin \n1-Bakiye goruntule \n2-Para cek \n3-Para Yatir \n4-Cikis yap")
        try:
            operation = int(input("Isleminizi tuslayin= "))
        except ValueError:
            print("Gecersiz islem tusladiniz!")
            continue
        if operation == 1:
            print("Bakiyeniz= ", budget)
        elif operation == 2:
            try:
                with_drawal = int(input("Cekmek istediginiz tutari giriniz= "))
            except ValueError:
                print("Gecersiz giris!")
                continue
            if with_drawal > 0:
                if with_drawal > budget:
                    print("Hesabinizda bu kadar para bulunmamaktadir")
                else:
                    budget -= with_drawal
                    print("Islem sonucu bakiye =", budget)
            else:
                print("Tutar sifirdan buyuk olmali!")
        elif operation == 3:
            try:
                deposit = int(input("Yatirmak istediginiz tutari giriniz= "))
            except ValueError:
                print("Gecersiz giris!")
                continue
            if deposit > 0:
                budget += deposit
                print("Islem sonucu bakiye =", budget)
            else:
                print("Gecersiz tutar girdiniz!")
        elif operation == 4:
            print("Gorusmek uzere")
        else:
            print("Gecersiz islem tusladiniz!")

while True:
    password_entry = getpass.getpass("Hosgeldiniz, Sifrenizi giriniz= ")
    if config.password == password_entry:
        while True:
            try:
                budget = int(input("Bakiyenizi giriniz= "))
                if budget < 0:
                    print("Gecersiz tutar girdiniz!")
                    continue
                break
            except ValueError:
                print("Gecersiz tutar girdiniz!")
                continue
        bank(budget)
        break
    else:
        print("Yanlis sifre!")
        continue