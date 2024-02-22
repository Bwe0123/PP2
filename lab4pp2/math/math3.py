from math import tan,pi
n=int(input("Input number of sides:"))
a=int(input("Input the length of a side:"))
r=a/tan(pi/n)/2
p=n*a
print("The area of the polygon is:",int(r*p/2))