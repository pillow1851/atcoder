N = int(input())
for i  in range(1,10):
    if N%i ==0:
        if 1<=N//i<=9:
            print("Yes")
            exit()
print("No")
