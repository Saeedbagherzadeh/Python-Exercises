a = float(input("enter a : "))
b = float(input("enter b : "))
c = float(input("enter c : "))


if (a + b < c)and(a + c < b)and(b + c < a) :
    print("these numbers cannot from a triangle" )

else :
    print("these numbers can form triangle")