from app.commands import Command

class AddCommand(Command):
    def execute(self, *args):
        try:
            numbers = [float(arg) for arg in args]
            result = sum(numbers)
            print(f"Result: {result}")
        except ValueError:
            print("Error: All arguments must be numbers.")

class ExamplePlugin:
    def square(self, x):
        return x * x

    def cube(self, x):
        return x * x * x