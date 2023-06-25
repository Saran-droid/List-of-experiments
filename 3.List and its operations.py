print( "a) Program for positive and negative indexing")
a = list(range(10))
print(a)
print("Positive indexing ...")
print("a[5]:",a[5])
print("a[9]:",a[9])
print(f"a[0:5]:{a[0:5]}")
print("Negative indexing ...")
print("a[-1]:",a[-1])
print("a[-4]:",a[-4])

print("b)Program to find whether the given list is in ascending order or not")
flag = 1
b = list(map(int,input("Enter the elements of a list:")))
def if_ascen(b):
    for i in range(len(b)):
        if b[i]> b[i+1]:
            return False
        else:
            return True
if (if_ascen(b)):
    print("The given list is in ascending order")
else:
    print("The given list is not in ascending order")
