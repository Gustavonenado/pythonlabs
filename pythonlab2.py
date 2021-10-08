
print("input a1 and press Enter:")
a1 = float(input())
print("input a2 and press Enter:")
a2 = float(input())
print("input a3 and press Enter:")
a3 = float(input())
print("input b1 and press Enter:")
b1 = float(input())
print("input b2 and press Enter:")
b2 = float(input())
print("input b3 and press Enter:")
b3 = float(input())
if((a1 / b1 == a2 / b2) and (a2 / b2 == a3 / b3)):
    print("vectors are collinear")
else:
    print("vectors are non-collinear")