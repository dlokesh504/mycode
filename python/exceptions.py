print("open a file or open database connection")
try:
    a = int(input("enter the value of A"))
    b = int(input("enter the value of B"))
    print(a // b)
except ZeroDivisionError as e:
    print("cans divid by zero", e)
except ValueError as e:
    print("user enterd invalid data:", e)
except Exception as e:
    print("something went wrong :", e)
finally:
    print("closing file and dabase connection")
