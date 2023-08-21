pt=input("Enter a plain text:")
key=input("Enter keyword:")
x=[]
k=list(key)
c=list(key)
for i in range(65,91):
    y=chr(i)
    x.append(y)

for i in range(len(x)):
    if x[i] not in k:
        char=x[i]
        c.append(char)
for i in range(len(pt)):
    char1=pt[i]
    for j in range(len(x)):
        if char1=x[i]:
            n=


    

print("Alphabets:",x)
print("Keyword:",k)
print("Cipher text:",c)
        
    
