w=int(input("Enter your weight(kg): "))
h=float(input("Enter your heght(m) : " ))
mbi=w/(h*2)
print("your mbi =",mbi)
if mbi<18.5:
    print("weight loss")
    if 18.5<mbi>24.9:
        print("normal weight")
    if 25<mbi>29.9:
        print("overweight")
    if 30<mbi>34.9:
        print("obesity")
    if mbi>35:
        print("overweight")