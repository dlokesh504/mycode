# linear search

def search(list, key):
    for i in range(0, len(list)):
        if list[i] == key:
            return True
    return False


list = [10, 20, 4, 40, 50, 60, 70, 80, 90]
n = int(input("enter the vale to be search"))
if search(list, n):
    print("element found in list")
else:
    print("element not found")
