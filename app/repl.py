from calculator.calculator import Calculator
from app.plugins.plugin_loader import load_plugins

class REPL:
    def __init__(self):
        self.calculator = Calculator()
        self.plugins = load_plugins() 
        print(f"Loaded plugins: {[plugin.get_command_name() for plugin in self.plugins]}") 

    def start(self):
        print("Calculator REPL. Type 'quit' to exit.")
        while True:
            command = input("Enter command (add, subtract, multiply, divide, history, clear, load, delete, greet, menu, quit): ").strip().lower()
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
                self.calculator.show_history()
            elif command == "clear":
                self.calculator.clear_history()
            elif command == "load":
                self.calculator.load_history()
            elif command == "delete":
                self.calculator.delete_history_file()
            elif command == "greet":
                name = input("Enter your name: ")
                greet_plugin = next((plugin for plugin in self.plugins if plugin.get_command_name() == "greet"), None)
                if greet_plugin:
                    print(greet_plugin.execute(name))
                else:
                    print("Greet plugin not found.")
            elif command == "menu":
                menu_plugin = next((plugin for plugin in self.plugins if plugin.get_command_name() == "menu"), None)
                if menu_plugin:
                    print(menu_plugin.execute())
                else:
                    print("Menu plugin not found.")
            elif command == "quit":
                print("Exiting calculator.")
                break
            else:
                print("Unknown command.")


if __name__ == "__main__":
    repl = REPL()
    repl.start()
