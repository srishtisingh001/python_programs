import cmath
a=float(input("enter value of 'a' "))
b=float(input("enter value of 'b' "))
c=float(input("enter value of 'c' "))
d=(b**2)-(4*a*c)
x1=(-b-cmath.sqrt(d))/(2*a)
x2=(-b+cmath.sqrt(d))/(2*a)
print("answer of this quadratic equation are {0} and {1}".format(x1,x2))
