from cal_art import logo
print(logo)

def add(n1,n2):
    return n1 + n2

def subt(n1, n2):
    return n1 - n2

def mult(n1,n2):
    return n1 * n2

def div(n1,n2):
    return n1 / n2

operations ={
    "+": add,
    "-": subt,
    "*": mult,
    "/": div
}

def calculator():
    calc = True
    num1 = int(input("What is the first number? "))

    while calc == True:
        num2 = int(input("What is the next number?" ))
        
        for operation in operations:
            print(operation)

        oper = input("Pick one operation from above? ")

        answer = operations[oper]
        answer = answer(num1,num2)

        print(answer)
        yon =input("Type 'yes' to continue and type 'no' to start over!!")
        if yon.lower() == "yes":
            num1 = answer
        elif yon.lower() == "no":
            calculator()

calculator()