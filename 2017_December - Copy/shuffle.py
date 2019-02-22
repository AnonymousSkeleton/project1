"""
ID: jasonja2
LANG: PYTHON3
TASK: shuffle
"""
fin = open ('shuffle.in', 'r')
fout = open ('shuffle.out', 'w')

a = int(fin.readline().strip())
blist = list(int(elem)-1 for elem in fin.readline().strip().split())
clist = list(int(elem) for elem in fin.readline().strip().split())
#dlist = clist[::1]

dicto = {blist[i] : i for i in range(a)}

for i in range(3):
    #for j in range(len(clist)):
    dlist = clist[:]
    for k, v in dicto.items():
        dlist[v] = clist[k]  #  this will mix up
    clist = dlist

for i in dlist:
    fout.write(str(i) + '\n')
