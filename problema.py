#sa se scrie cate litere mari sunt
#in fisierul litereA.txt,cate litere mici in litereB
#in cifre.txt cate cifre sunt
#si cate caractere in caractere.txt

with open("input.txt","r") as f: 
    sir=f.readline()
nrm=0
nr=0
n=0
ns=0
for i in sir:
    if ord(i) in range(65,91):
        nrm+=1
with open("litereA.txt","w") as f:
    f.write(str(nrm))
for i in sir:
    if ord(i) in range(97,123):
        nr+=1
with open("litereB.txt","w") as f:
    f.write(str(nr))
for i in sir:
    if ord(i) in range(49,58):
        n+=1
with open("cifre.txt","w") as f:
    f.write(str(n))
for i in sir:
    if ord(i) in range(33,42):
        ns+=1
with open("caractere.txt","w") as f:
    f.write(str(ns))
