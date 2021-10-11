# group creation by loop and conditional statement.

a= int(input(" enter number  "))
b=("grade-A","grade-B","grade-C","grade-D")

for i in [b]:
    if (a>=90):
        print(b[0])
    elif (a>=80):
        print(b[1])
    elif (a>=70):
        print(b[2])
    elif (a>=60):
        print(b[3])
    else:
        print("fail")
