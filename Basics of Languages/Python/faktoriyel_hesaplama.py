def faktoriyel(n):
#faktoriyel fonksiyonuna n parametresi tanımlıyoruz
    if n == 0:
    #n parametresi eğer 0 ise
        return 1
        #fonksiyon 1 sonucunu versin
    else:
    #eğer değilse
        return n*faktoriyel(n-1)
        #fonksiyonun sonucu olarak:
        #fonksiyonun parametresini, parametresinin bir eksiğiyle çarp
    
numara = int()
input("Faktoriyelini hesaplamak istediğiniz sayıyı girin: ")
print(f"{numara}! = {faktoriyel(numara)}")
