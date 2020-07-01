from itertools import permutations 
 

print(""" \n\n              
      **        **          
      ******  * **  ****  ****
      **  **    **  *     *
      **  **    **  *     *    
                             h1rr v0.2\n\n\n""")


i = ''
veriler = []

print("You can end giving keys with 'cik' command")
while i != 'cik':
    i = input("Give a key : ")
    veriler.append(i) 
    print(veriler) 
veriler.pop()

limit = input("\nChoose the value of delimeter that will determine how many keys will be used\n(If you do not give a number, it will use all the keys)\n: ")
if limit == '':
    limit = int(len(veriler))
limit = int(limit)

filename = input("\nEnter your file name if you want to create a txt file that includes the wordlist\n(If you do not enter a name, it will not create a file that includes the wordlist)\n: ")
 
for n in range(1,limit+1):
    perm = permutations(veriler, n) 
  
 
    for i in list(perm): 
        thekey = "".join(list(i))
        print(thekey)
        
        if filename == '':
            continue
        else:
            file = open(f"{filename}.txt", "a") # burada masaustune olusturmam gerekiyor!!
            file.write(f"{thekey}\n") 
file.close() 
    