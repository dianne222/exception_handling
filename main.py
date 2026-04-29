class UserInput:
    def choose_math_operation(self):
        print("Choose math operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")

        choice = int(input("Enter number of your choice: "))
        print(choice)
        return choice

calculator = UserInput()
calculator.choose_math_operation()

