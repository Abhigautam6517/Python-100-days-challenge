a = input("Enter your Good name \n")
print("Hello " + a +" " + "Sir")
print("Thank You for using BMI Calculator.......")
w = int(input("Enter your Weight in (Kg)"))  #w=Weight
h = float(input("Enter your Height in (metre)"))  #h = Height

bmi = float(w/h**2)
print(bmi)


if(bmi<18.0):
    print("Underweight")
elif(bmi>24.9):
    print("Normal Range")
elif(bmi>29.9):
    print("Overweight")
else:
    print("Obese")

print("Thank You For using this app....!")
