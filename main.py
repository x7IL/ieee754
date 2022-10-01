


a,d = map(int,str(142.7).split("."))
sign = (a>0)*str(0) or str(1)
binaire = bin(a)[2:]

sn=str(sign)
expo = bin(127+len(binaire)-1)[2:]
c = ''
d= float('0.'+str(d))
for i in range(23):
    d = d*2
    c+=str(d)[0]
    if int(str(d)[0]) > 0:
        d = float('0.'+str(d)[-1])
scientific = binaire[1:]
res=sn+" "+expo+" "+binaire[1:]+c
print(res)

#0 10000111 00000111010011001100110
#0 10000111 0000011101001100110011001100110

