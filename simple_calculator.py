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
                print(choice)
                return choice
            else:
                raise Exception("invalid choice")
        except ValueError:
            print("Please enter a Number")
        except:
            print("Invalid Choice")


    def get_two_numbers(self):
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            return num1, num2
        except ValueError:
            print("Please enter a Number")

calculator = UserInput()
calculator.choose_math_operation()
calculator.get_two_numbers()

