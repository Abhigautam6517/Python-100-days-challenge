# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
if(year%4==0 and year%100==0 and year%400==0):
  print("This Year is Leap year")
else:
  print("This year is not leap year")



