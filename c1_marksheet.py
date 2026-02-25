# mark sheet

english = int(input("enter marks for english: "))
urdu = int(input("enter marks for urdu: "))
maths = int(input("enter marks for maths: "))
computer = int(input("enter marks for computer: "))
science = int(input("enter marks for science: "))

obtained = english + urdu + maths + computer + science

percentage = (obtained / 5) * 100

print("total marks are:", obtained)
print("percentage is:", percentage)
