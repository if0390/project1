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
            if not self.calculator.history:
                print("No calculations in history.")
            else:
                print("Calculation History:")
                for entry in self.calculator.history:
                    operation = entry["operation"]
                    operand1 = entry["operand1"]
                    operand2 = entry["operand2"]
                    result = entry["result"]
                    print(f"{operation.title()} {operand1} and {operand2} = {result}")
        elif command == "quit":
            print("Exiting calculator.")
            break
        else:
            print("Unknown command.")