"""
ID: jasonja2
LANG: PYTHON3
TASK: billboard
"""
fin = open ('billboard.in', 'r')
fout = open ('billboard.out', 'w')

alist = list(int(elem) for elem in fin.readline().strip().split())
blist = list(int(elem) for elem in fin.readline().strip().split())

def area(abc):
    return (abc[2]-abc[0]) * (abc[3]-abc[1])

area1 = area(alist)
area2 = area(blist)

def over(a,b): 
    # find out if there is no overlap. If so, return 0
    # if (((a[2] <= b[0]) and (a[3] <= b[1])) \
    # or ((b[2] <= a[0]) and (a[3] <= b[1])) or \
    #     ((a[2] <= b[0]) and (b[3] <= a[1])) or \
    #         ((b[2] <= a[0]) and (b[3] <= a[1]))):
    #     return 0

    """if (max(point_lst1[2], point_lst2[0]) == point_lst2[0]) \
            or (max(point_lst1[0], point_lst2[2]) == point_lst1[0]) :  # when truck is outside of bbd.
        return 0"""
    
    #Teacher's code for seeing if there is any overlap
    if (a[2]< b[0] or b[2] < a[0]) or \
       (a[3]< b[1] or b[3] < a[1]) :
       return 0

    # there is overlap, follow the algo

    dlist = list()
    dlist.append(max(a[0],b[0]))
    dlist.append(max(a[1],b[1]))  
    dlist.append(min(a[2],b[2]))
    dlist.append(min(a[3],b[3]))

    d = area(dlist)
    return area(dlist)

a = over(alist,blist)

print(a)