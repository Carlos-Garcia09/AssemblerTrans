
p=hex(16384)[2:]
li2="2"
for i in range(0,10):
    p=hex(int(p,16)+int(li2,16))[2:]
    print(p)