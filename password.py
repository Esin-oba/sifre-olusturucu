import random

uzunluk = int(input("şifrenizin uzuluğu nasıl olsun?"))
sifre = ""
sembol = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
for i in range(uzunluk):
    sifre += random.choice(sembol)
print("şifreniz:", sifre)              
