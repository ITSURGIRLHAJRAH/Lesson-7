h=float(input("Enter height in metres: "))
w=int(input("Enter weight in kg: "))
bmi=w/(h*h)
print("BMI is ", bmi)
if bmi<18:
    print("Person is underweight, eat food, string ✌🏽")
elif bmi>=18 and bmi<25:
    print("Person has normal weight, good job 👍🏽")
elif bmi>=25 and bmi<30:
    print("Person is overweight, need exercise 😼")
else:
    print("Person is OBESE, oh no 😰")