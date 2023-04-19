
# Bana soru sormak için veya daha fazla türkce kaynak için instagram ve GitHub da takip edebilirsin.
# github.com/canemingozde
# instagram.com/canemingozde


def ikilik():
    while True:
        girdi = input("Binarye çevirmek istediniz sayıyı yazınız işlevi değiştirmek için ise close yazınız: ")
        if girdi == "close":
            break
        else:
            cevir = bin(int(girdi))
            print(cevir)
            

def onluk():
    while True:
        girdi2 = input("Decimale çevirmek istediniz sayıyı yazınız işlevi değiştirmek için ise close yazınız: ")
        if girdi2 == "close":
            break
        else:        
            cevir = int(girdi2,2)
            print(cevir)


while True:
    print("****** Decimale çevirmek için 10 yazın | Binary çevirmek için 2 yazın | Kapatmak için close yazın ******")
    print()
    istek = input("Hangi işlemi yapmak istiyorsunuz: ")
    if istek == "2":
        ikilik()
    elif istek == "10":
        onluk()
    elif istek == "close":
        break

