def pattern (N):
    if N==0:
        return 
    print("*" * N)
    pattern(N-1)

N= int(input("Enter your number "))
print(pattern(N))