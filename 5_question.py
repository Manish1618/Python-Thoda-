def inch(I):
    if I==0:
        print("Not possible")
    return I*2.54
I=float(input("Enter which to convert : "))
print(f"{round(inch(I),2)}cm")