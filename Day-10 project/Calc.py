def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    return a/b

operation = {
    "+":add,
    "-":sub,
    "*":mul,
    "/":div,
}
def calculator():
    num1 = float(input("Ente first number \n"))


    for symbol in operation:
        print(symbol)
    should_continue=True

    while should_continue:
        pick = input("Enter the symbol who you pick out")
        num2 = float(input("Enter the next number \n"))
        calculation_function = operation[pick]
        answer  = calculation_function(num1,num2)

        print(f"{num1} {pick} {num2} = {answer}")

        if input(f"Type 'y' to continue and Type 'n' to new calculator ")=='y':
            num1=answer
        else:
            should_continue=False
            calculator()
calculator()
        

# pick = input("Enter the symbol who you pick out")
# num3 = int(input("Enter second number"))
# calculation_function = operation[pick]
# answer2  = calculation_function(answer,num2)
# print(answer2)
