import logging
from app.commands import Command

class HistoryCommand(Command):
    def __init__(self, calculator):
        self.calculator = calculator

    def execute(self, *args):
        history = self.calculator.history
        if history.empty:
            print("No calculations in history.")
        else:
            print("Calculation History:")
            print(history.to_string(index=False))  