year = input("Enter the year:")
age = 2023 - int(year)
print(age)

first = int(input("First:"))
second = float(input("Second:"))
sum = first + second
print(sum)

weight = int(input("Enter the weight:"))
unit = (input("weight in K(kg) or L(lbs):"))
if unit.upper() == "K":
    converted = weight / 0.45
    print("Weight in Lbs: " + str(converted))
else:
    converted = weight*0.45
    print("Weight in kgs: " + str(converted))
