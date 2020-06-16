
from itertools import permutations 
 
print("h1rr v0.1")

i = ''
veriler = []

print("cik komutu ile eklenti vermeyi bitirebilirsiniz")
while i != 'cik':
    i = input("Eklenti giriniz : ")
    veriler.append(i) 
    print(veriler) 
veriler.pop()

limit = int(input("Bir arada kullanilacak max eklenti sayisini seciniz : "))

for n in range(1,limit+1):
    perm = permutations(veriler, n) 
  
 
    for i in list(perm): 
        print("".join(list(i)))
    