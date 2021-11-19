
print("input n and press Enter:")
n = int(input())
print("input m and press Enter:")
m = int(input())
L = int
D = int
S = int
for i in range (1, m):
    S = 0
    L = i
    while (L > 0):
        D = L % 10
        L = L // 10
        S = S + D
    if S == n : 
             print(i)
          
