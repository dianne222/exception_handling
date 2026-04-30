class UserInput:
    def choose_math_operation(self):
        print("Choose math operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")

        try:
            choice = int(input("Enter number of your choice: "))
            if 1 <= choice <= 4:
                return choice
            else:
                raise ValueError("invalid choice")
        except:
            print("Invalid Choice")

    def get_two_numbers(self):
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            return num1, num2
        except ValueError:
            print("Please enter a Number")

class SolveOperation(UserInput):
    def addition(self, addends1, addends2):
        return addends1 + addends2

    def subtraction(self, minuend, subtrahend):
        return minuend - subtrahend

    def multiplication(self, multiplicand, multiplier):
        return multiplicand * multiplier

    def division(self, dividend, divisor):
        try:
            quotient = dividend / divisor
            return quotient

        except ZeroDivisionError:
            print("Cannot divide by zero")

    def operations(self, choice, num1, num2):
        if choice == 1:
            return self.addition(num1, num2)
        elif choice == 2:
            return self.subtraction(num1, num2)
        elif choice == 3:
            return self.multiplication(num1, num2)
        elif choice == 4:
            return self.division(num1, num2)

class Calculator(SolveOperation):
    def calculate(self):
        continue_choice = "y"
        while continue_choice == "y":
            choice = self.choose_math_operation()
            num1, num2 = self.get_two_numbers()

            result = self.operations(choice, num1, num2)
            print(result)
            continue_choice = input("Do you want to continue?(y/n): ").lower().strip()

        print("Thank you for using this calculator")

calculator = Calculator()
calculator.calculate()