import logging

class Calculator:
    def __init__(self):
        self.history = []

    def add(self, x, y):
        result = x + y
        self._save_history("add", x, y, result)
        return result

    def subtract(self, x, y):
        result = x - y
        self._save_history("subtract", x, y, result)
        return result

    def multiply(self, x, y):
        result = x * y
        self._save_history("multiply", x, y, result)
        return result

    def divide(self, x, y):
        try:
            result = x / y
            self._save_history("divide", x, y, result)
            return result
        except ZeroDivisionError:
            logging.error("Attempted to divide by zero")
            return "Error: Division by zero"

    def _save_history(self, operation, x, y, result):
        entry = {"operation": operation, "operand1": x, "operand2": y, "result": result}
        self.history.append(entry)
        logging.info(f"Recorded in history: {entry}")