#!/usr/bin/env python3
strain=[]
pangenome=[]
#with open("all.designMatrix.elements", "r") as f:
with open("try", "r") as f:
    num=1
    strain.append(num)
    for line in f:
        words=line.rstrip().split()
        #print(words[1])
        if(words[1]==num):
                strain.append(words[0])
        else:
            num +=1
            nexd = '\t'.join(str(s) for s in strain)
            strain=[]
            pangenome.append(nexd)
            strain.append(num)



thefile = open('test', "w")
for item in pangenome:
    thefile.write(item)
    thefile.write("\t")
thefile.close()
