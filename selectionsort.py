def selection(list):
    for i in range(len(list)-1):
        minpos = i
        for j in range(i,len(list)):
            if list[j]<list[minpos]:
                minpos=j
        temp= list[i]
        list[i]=list[minpos]
        list[minpos]=temp
    return  list







nums=[2,8,1,5,7,5,500,588,0]
print(selection(nums))
