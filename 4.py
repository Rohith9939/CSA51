pt = input("Enter plain text: ").upper()
key = input("Enter the key: ").upper()
print(pt)
p=list(pt)
x=list(key)
size=int(len(p)/len(x))+1
k=list()
e=[]
d=[]
for i in range(size):            
    k.extend(x)
for i in range(len(pt)):
    x=chr(((ord(p[i])-65)+(ord(k[i]))-65)%26+65+1)
    e.append(x)
for i in range(len(pt)):
    x=chr(((ord(p[i])-65)-(ord(k[i]))-65)%26+65+1)
    d.append(x)
print("Encrypted message:",e)
print("Decrypted message:",d)
