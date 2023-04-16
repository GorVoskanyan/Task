def kentZuyg(number):
    bn=str(bin(number))
    bn=bn[2:]
    bn=bn[::-1]
    lst=[0,0]
    for i in range(0,len(str(bn)),2):
        lst[0]+=int(bn[i])
    for i in range(1,len(str(bn)),2):
        lst[1]+=int(bn[i])
    return lst

print(kentZuyg(19))




def mat(lst):
    '''Given a m x n binary matrix mat, find the 0-indexed 
    position of the row that contains the maximum count of ones,
      and the number of ones in that row.
    In case there are multiple rows that have the maximum count of ones,
      the row with the smallest row number should be selected.
    Return an array containing the index of the row, and the number of ones in it.'''
    k=[]
    for i in range(len(lst)):
        k.append(sum(lst[i]))
    num=0
    max=k[0]
    for i in range(len(k)):
        if k[i]>max:
            max=k[i]
            num=i
    return [num,max]

print(mat([[0,1],[1,0]]))
        


