english = int(input("enter marks for english: "))
urdu = int(input("enter marks for urdu: "))
maths = int(input("enter marks for maths: "))
computer = int(input("enter marks for computer: "))
science = int(input("enter marks for science: "))

obtained = english + urdu + maths + computer + science
percentage = (obtained / 500) * 100

if 80 <= percentage <= 100:
    print("Excellent job, A+")
elif 60 <= percentage < 80:
    print("Good job, A")
elif 40 <= percentage < 60:
    print("Needs improvement, B")
elif 30 <= percentage < 40:
    print("Needs lots of improvement, C")
else:
    print("Fail, F")

print("total marks are:", obtained)
print("percentage is:", round(percentage, 2))
