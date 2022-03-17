import random
names_string = input("Give me everbody names , seperated by a comma \n ")
names = names_string.split(",")
print(names)
# num_items = len(names)
# random_num = random.randint(0, num_items-1)
# person_who_bill_pay = names[random_num]
# print(person_who_bill_pay + " " + "going to buy some meal today")

person = random.choice(names)
print(person)