from app.commands import Command

class AddCommand(Command):
    def execute(self, *args):
        # Convert arguments to floats and perform addition
        try:
            numbers = [float(arg) for arg in args]
            result = sum(numbers)
            print(f"Result: {result}")
        except ValueError:
            print("Error: All arguments must be numbers.")