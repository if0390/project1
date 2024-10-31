from calculator.calculations import Calculations
from calculator.calculation import Calculation
from calculator.operations import add, subtract, multiply, divide
from decimal import Decimal
import logging

class Calculator:
    def add(self, x, y):
        calculation = Calculation.create(Decimal(x), Decimal(y), add)
        result = calculation.perform()
        Calculations.add_calculation(calculation)
        logging.debug(f"Addition result: {result} added to history")
        return result

    def subtract(self, x, y):
        calculation = Calculation.create(Decimal(x), Decimal(y), subtract)
        result = calculation.perform()
        Calculations.add_calculation(calculation)
        logging.debug(f"Subtraction result: {result} added to history")
        return result

    def multiply(self, x, y):
        calculation = Calculation.create(Decimal(x), Decimal(y), multiply)
        result = calculation.perform()
        Calculations.add_calculation(calculation)
        logging.debug(f"Multiplication result: {result} added to history")
        return result

    def divide(self, x, y):
        try:
            calculation = Calculation.create(Decimal(x), Decimal(y), divide)
            result = calculation.perform()
            Calculations.add_calculation(calculation)
            logging.debug(f"Division result: {result} added to history")
            return result
        except ValueError:
            logging.error("Attempted to divide by zero")
            return "Error: Division by zero"

    @property
    def history(self):
        return Calculations.get_history()
