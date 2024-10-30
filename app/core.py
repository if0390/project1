import logging
from decimal import Decimal
from calculator.calculation import Calculation
from calculator.operations import add, subtract, multiply, divide

class Calculator:
    def __init__(self):
        self.history = []

    def add(self, x, y):
        calculation = Calculation.create(Decimal(x), Decimal(y), add)
        result = calculation.perform()
        self._save_history("add", x, y, result)
        return result

    def subtract(self, x, y):
        calculation = Calculation.create(Decimal(x), Decimal(y), subtract)
        result = calculation.perform()
        self._save_history("subtract", x, y, result)
        return result

    def multiply(self, x, y):
        calculation = Calculation.create(Decimal(x), Decimal(y), multiply)
        result = calculation.perform()
        self._save_history("multiply", x, y, result)
        return result

    def divide(self, x, y):
        try:
            calculation = Calculation.create(Decimal(x), Decimal(y), divide)
            result = calculation.perform()
            self._save_history("divide", x, y, result)
            return result
        except ValueError as e:
            logging.error("Attempted to divide by zero")
            return "Error: Division by zero"

    def _save_history(self, operation, x, y, result):
        entry = {"operation": operation, "operand1": x, "operand2": y, "result": result}
        self.history.append(entry)
        logging.info(f"Recorded in history: {entry}")
