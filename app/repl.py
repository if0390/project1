from app.core import Calculator

class REPL:
    def __init__(self):
        self.calculator = Calculator()
    
    def start(self):
        print("Calculator REPL. Type 'quit' to exit.")
        while True:
            command = input("Enter command (add, subtract, multiply, divide, history, quit): ").strip().lower()
            if command in ["add", "subtract", "multiply", "divide"]:
                x = float(input("Enter first number: "))
                y = float(input("Enter second number: "))
                if command == "add":
                    result = self.calculator.add(x, y)
                elif command == "subtract":
                    result = self.calculator.subtract(x, y)
                elif command == "multiply":
                    result = self.calculator.multiply(x, y)
                elif command == "divide":
                    result = self.calculator.divide(x, y)
                print(f"Result: {result}")
            elif command == "history":
                print("Calculation History:")
                for entry in self.calculator.history:
                    print(entry)
            elif command == "quit":
                print("Exiting calculator.")
                break
            else:
                print("Unknown command.")