import operator
import art

operations = {
        "+": operator.add, "-": operator.sub,
        "*": operator.mul, "/": operator.truediv}


def calculation(n1, n2, operation):
    return operations[operation](n1, n2)


choice = 'n'
print(art.logo)


def calculator():

    should_accumulate = True
    num1 = float(input("What is the first number?: "))

    while should_accumulate:

        for symbol in operations:
            print(symbol)
        operation = input("Pick an operation: ")
        num2 = float(input("What's the next number: "))
        answer = calculation(num1, num2, operation)

        print(f"{num1} {operation} {num2} = {answer}")

        choice = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ").lower()

        if choice == 'y':
            num1 = answer
            print(f"Third number {num1} ")
        else:
            should_accumulate = False
            print("/n" * 20)
            calculator()


calculator()
