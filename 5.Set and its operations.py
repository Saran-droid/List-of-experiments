# Python program to check whether the given set is a subset of another set
set1 =set(map(int,input("Enter the elements of the first set:")))
print(f"The first set is : {set1}")
set2 =set(map(int,input("Enter the elements of the second set:")))
print(f"The second set is : {set2}")
if set2.issubset(set1):
    print("Set2 is a subset of Set1")
else:
    print("Set2 is not a subset of Set1")