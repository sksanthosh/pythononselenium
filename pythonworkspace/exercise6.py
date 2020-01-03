#Take 3 sides of the triangle, and decide whether it is SCALENE, EQUILATERAL or ISOSCELES

s1=int(input("Enter the first side number of triangle: "))
s2=int(input("Enter the second side number of triangle: "))
s3=int(input("Enter the third side number of triangle: "))

if s1==s2==s3:
    print("It's a EQUILATERAL Triangle")
elif s1!=s2 and s1!=s3 and s2!=s3:
    print("It's a SCALENE Triangle")
else:
    if (s1==s2 and s1!=s3)or(s1==s3 and s1!=s2):
        print("It's a ISOSCELES Triangle")
    elif (s2==s1 and s2!=s3) or (s2==s3 and s2!=s1):
        print("It's a ISOSCELES Triangle")
    elif (s3==s1 and s3!=s2) or (s3==s2 and s3!=s1):
        print("It's a ISOSCELES Triangle")

   
