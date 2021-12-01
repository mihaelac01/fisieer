f=open("caracter.txt","w")
b=str(input("Introduceti un sir: "))
f.write(b)
f.close()

f=open("caracter.txt","r")
c=f.read()
print("Sirul:", c)
f.close()

v=[]
for i in range(0,len(c)):
    if str(c[i])=='o' or str(c[i])=='a' or str(c[i])=='e' or str(c[i])=='i' or str(c[i])=='u' or str(c[i])=='O' or str(c[i])=='A' or str(c[i])=='E' or c[i]=='I' or c[i]=='U':
        v.extend(c[i])

nr=str(len(v))      
f=open("vocale.txt","w")
f.write(str(v))
f.write('\n')
f.write('Numarul de vocale din sir: ')
f.write(nr)
f.close()

f=open("vocale.txt","r")
m=f.read()
print("Vocalele din sir sunt:", m)
f.close()