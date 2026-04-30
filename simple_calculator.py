class UserInput:
    def choose_math_operation(self):
        while True:
            print("-" * 26)
            print("| Choose math operation: |")
            print("|" + "-" * 24 + "|")
            print("| 1. Addition            |")
            print("| 2. Subtraction         |")
            print("| 3. Multiplication      |")
            print("| 4. Division            |")
            print("|" + "-" * 24 + "|")
            print("| 0. Exit                |")
            print("-" * 26)

            try:
                choice = int(input("Enter number of your choice: "))
                if 0 <= choice <= 4:
                    return choice
                else:
                    raise ValueError("invalid choice")

            except:
                print("Invalid Choice")

    def get_two_numbers(self):
        while True:
            try:
                print("-" * 30)
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
                print("-" * 30)
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

        except ZeroDivisionError:
            quotient = "Cannot divide by zero"
        return quotient

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
    # def display_result(self):
    #     print("\n")

    def calculate(self):
        continue_choice = "y"
        while continue_choice == "y":
            choice = self.choose_math_operation()
            if choice == 0:
               break
            num1, num2 = self.get_two_numbers()

            result = self.operations(choice, num1, num2)
            len_num1 = len(str(num1)) + 21
            len_num2 = len(str(num2)) + 21
            if len_num1 > len_num2:
                border = "-" * len_num1
            else:
                border = "-" * len_num2
            if len(str(num1)) > len(str(num2)):
                if ((len(str(num1)) - len(str(num2))) % 2) != 0:
                    spacing2 = " " * (int((len(str(num1)) - len(str(num2))) / 2) + 1)
                    spacing2a = " " * int((len(str(num1)) - len(str(num2))) / 2)
                else:
                    spacing2 = " " * int((len(str(num1)) - len(str(num2))) / 2)
                    spacing2a = spacing2
                spacing1 = " " * 0
                spacing1a = " " * 0
                print(spacing2)
            else:
                if ((len(str(num2)) - len(str(num1))) % 2) != 0:
                    spacing1 = " " * (int((len(str(num2)) - len(str(num1))) / 2) + 1)
                    spacing1a = " " * int((len(str(num2)) - len(str(num1))) / 2)
                else:
                    spacing1 = " " * int((len(str(num2)) - len(str(num1))) / 2)
                    spacing1a = spacing1
                spacing2 = " " * 0
                spacing2a = " " * 0

            print(border)
            print(f"| First Number:  | {spacing1a}{num1}{spacing1} |")
            print(border)
            print(f"| Second Number: | {spacing2a}{num2}{spacing2} |")
            print(border)
            print(f"| Result:        | {result} |" )
            print(border)

            while True:
                continue_choice = input("Do you want to continue?(y/n): ").lower().strip()
                if continue_choice == "n":
                    break
                elif continue_choice == "y":
                    break
                else:
                    print("Invalid Choice")


        print("Thank you for using this calculator")

calculator = Calculator()
calculator.calculate()