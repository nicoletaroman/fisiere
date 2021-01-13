with open("input.txt","r") as f:
    a=f.read()
    b=int(a)-2
    c=int(a)-1
    d=int(a)
    e=int(a)+1
    f=int(a)+2
with open("output.txt","w") as f:
    f.write(str(b))
    f.write(",")
    f.write(str(c))
    f.write(",")
    f.write(str(d))
    f.write(",")
    f.write(str(e))
    f.write(",")
    f.write(str(f))

    