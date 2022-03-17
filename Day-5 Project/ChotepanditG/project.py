import random
from typing import Sized
import boysDatabase
import GirkDB

# print(list1[2])]
print("Please Type boy or Girl......")
name = input("Enter your Gender \n").lower()
if (name=="boy"):
    print("wait.... I will Suggest Your Name")
    list1 = boysDatabase.boy_databse.split()
    random_name = random.randint(1,1877)
    print(list1[random_name])
elif (name=="girl"):
    print("wait.... I will Suggest Your Name")
    list2 = GirkDB.girl_database.split()
    random_name = random.randint(1,1756)
    print(list2[random_name])
else:
    print("please valid gender")

