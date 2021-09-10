import math

# Grade	Scale	Grade Description	US Grade
# A	75.00 - 100.00	Distinction	A
# B	65.00 - 74.99	Very Good Pass	B
# C	55.00 - 64.99	Credit Pass	C
# S	40.00 - 54.99	Ordinary Pass	D
# W	0.00 - 39.99	Failure	F


marks=float(input("Enter your marks: "))
rounded_marks=math.ceil(marks)

if   rounded_marks>=90:
     print("You have an excellent Pass(A+ pass)!")
elif rounded_marks>=75:
     print("You have a Distinction Pass(A pass)!")
elif rounded_marks>=65:
     print("You have Very Good Pass(B pass)!")
elif rounded_marks>=55:
     print("You have a Credit Pass(C pass)!")
elif rounded_marks>=40:
     print("You have an Ordinary Pass(S pass)!")
elif rounded_marks>=0:
     print("You have a Failure Pass(W pass)!")
else:
    print("Invaild")