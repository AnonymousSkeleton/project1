"""
ID: jasonja2
LANG: PYTHON3
TASK: measurement
"""
fin = open ('measurement.in', 'r')
fout = open ('measurement.out', 'w')

#HOW TO GET KEY WITH MAXIMUM VALUE IN DICT

# max(dict_a, key= lambda x: dict_a[x])
# max(dict_a, key= dict_a.get)


a = int(fin.readline().strip())
dicto = dict()
rdict = dict()
rdict1 = dict()
rdict2 = dict()

for i in range(a):
    templist = fin.readline().strip().split()
    dicto[int(templist[0])] = [(templist[1]),int(templist[2])]

rdict['Mildred'] = 7
rdict['Elsie'] = 7
rdict['Bessie'] = 7

rdict1['Elsie'] = 7
rdict1['Mildred'] = 7
rdict1['Bessie'] = 7

rdict2['Bessie'] = 7
rdict2['Elsie'] = 7
rdict2['Mildred'] = 7
    
day = 1
changes = 0
result = 1
leaderlistb = list()

while day <= 100:
    if day in dicto.keys():

        cow = (dicto[day])[0]
        milk = (dicto[day])[1]
        rdict[cow] = rdict[cow] + milk
        rdict1[cow] = rdict2[cow] + milk
        rdict2[cow] = rdict2[cow] + milk

        a = (max(rdict, key= lambda x: rdict[x]))
        b = (max(rdict1, key= lambda x: rdict1[x]))
        c = (max(rdict2, key= lambda x: rdict2[x]))

        aset = set([a,b,c])
        leaderlistb.append(aset)


        #Use max() function? - Find out if the cow display would need to be changed on a certain day
        #max(diction, ksy = lambda x: diction[x]) -> Try it, it may help

    day += 1

for i in range(len(leaderlistb)-1):
    if leaderlistb[i + 1] != leaderlistb[i]:
        result += 1
        
fout.write(str(result))

#_________________________________________________________________________#

#TEACHER'S CODE:

# fin = open('measurement.in', 'r')
# fout = open ('measurement.out', 'w')

# n = int(fin.readline())

# measurement = []
# names = set()
# for i in range(n):
#     line_lst = fin.readline().split()
#     measurement.append((int(line_lst[0]), line_lst[1], int(line_lst[2])))
#     names.add(line_lst[1])

# measurement.sort()
# display = list(names)
# diplay_change = 0

# measures_dict = { x: 7 for x in names}

# for day_, name_, change_  in measurement:
#   measures_dict[name_] += int(change_)
#   max_value = max(measures_dict.values())
#   tmp_to_comp = [k for k, v in measures_dict.items() if v == max_value]

#   if set(display) != set(tmp_to_comp):
#     diplay_change +=1
#     display = tmp_to_comp



