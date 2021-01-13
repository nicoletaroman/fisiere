
with open ("globulete.txt","r") as f:
    ga=f.readline()
    gr=int(ga)+3
    gal=int(ga)+int(gr)-2
    gt=int(ga)+int(gr)+int(gal)

with open ("bradut.txt","w") as f:
    f.write(str(gt))