#1.
matn = input("Matn kiriting: ")

harf_soni = sum(1 for b in matn if b.isalpha())
raqam_soni = sum(1 for b in matn if b.isdigit())
probel_soni = sum(1 for b in matn if b.isspace())

print("Harflar soni:", harf_soni)
print("Raqamlar soni:", raqam_soni)
print("Bo'shliqlar soni:", probel_soni)

#2.
n = int(input("Son kiriting: "))

juft_yigindi = 0
toq_yigindi = 0

for i in range(1, n + 1):
    if i % 2 == 0:
        juft_yigindi += i
    else:
        toq_yigindi += i

print("Juft sonlar yig'indisi:", juft_yigindi)
print("Toq sonlar yig'indisi:", toq_yigindi)


#3.
import random
import string

sirli_harf = random.choice(string.ascii_lowercase)

urinish = 0
chegara = 5
topildi = False

print("Kompyuter 1 ta ingliz harfini tanladi. Sizda 5 ta urinish bor!")

while urinish < chegara:
    kirit = input("Harf kiriting: ").lower()

    if len(kirit) != 1 or not kirit.isalpha():
        print("Faqat bitta harf kiriting!")
        continue

    urinish += 1

    if kirit == sirli_harf:
        print(f"Zo'r! Siz {urinish}-urinishda topdingiz ")
        topildi = True
        break
    else:
        print("Noto'g'ri. Yana urinib ko'ring.")

if not topildi:
    print(f"Afsus, topa olmadingiz. Sirli harf: {sirli_harf}")
