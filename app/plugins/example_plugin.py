from app.commands import Command

class AddCommand(Command):
    def execute(self, *args):
        try:
            numbers = [float(arg) for arg in args]
            result = sum(numbers)
            print(f"Result: {result}")
        except ValueError:
            print("Error: All arguments must be numbers.")

class SubtractCommand(Command):
    def execute(self, *args):
        try:
            numbers = [float(arg) for arg in args]
            if len(numbers) < 2:
                print("Error: Subtract requires at least two numbers.")
                return
            result = numbers[0] - sum(numbers[1:])
            print(f"Result: {result}")
        except ValueError:
            print("Error: All arguments must be numbers.")

class MultiplyCommand(Command):
    def execute(self, *args):
        try:
            numbers = [float(arg) for arg in args]
            result = 1
            for number in numbers:
                result *= number
            print(f"Result: {result}")
        except ValueError:
            print("Error: All arguments must be numbers.")

class DivideCommand(Command):
    def execute(self, *args):
        try:
            numbers = [float(arg) for arg in args]
            if len(numbers) < 2:
                print("Error: Divide requires at least two numbers.")
                return
            result = numbers[0]
            for number in numbers[1:]:
                if number == 0:
                    print("Error: Division by zero is not allowed.")
                    return
                result /= number
            print(f"Result: {result}")
        except ValueError:
            print("Error: All arguments must be numbers.")

class ExamplePlugin:
    def square(self, x):
        return x * x

    def cube(self, x):
        return x * x * x
