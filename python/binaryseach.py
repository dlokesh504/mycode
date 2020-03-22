pos = -1


def binarysearch(list, key):
    low = 0
    upper = len(list) - 1
    while low <= upper:
        mid = (low + upper) // 2
        #print(mid)
        if list[mid] == key:
            globals()['pos'] = mid
            return True,pos
        else:
            if list[mid] < key:
                low = mid + 1
            else:
                upper = mid - 1
    return False,pos


list = [10, 20, 4, 40, 50, 60, 70, 80, 90]
n = int(input("enter the vale to be search"))
if binarysearch(list, n):
    print("element found in list : at",pos+1)
else:
    print("element not found")
