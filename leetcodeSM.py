def kentZuyg(number):
    bn=str(bin(number))
    bn=bn[2:]
    bn=bn[::-1]
    lst=[0,0]
    for i in range(len(str(bn))):
        if bn[i]=='1' and int(i)%2==0:
            lst[1]+=1
        elif bn[i]=='1' and int(i)%2!=0:
            lst[0]+=1
    return lst

print(kentZuyg(2))