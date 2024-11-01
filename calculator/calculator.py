import pandas as pd
import os
import logging

class Calculator:
    def __init__(self):
        self.history_file = "history.csv"
        self.history = self.load_history()
        logging.info("Calculator initialized.")

    def add(self, a, b):
        result = a + b
        self.update_history(f"{a} + {b}", result)
        logging.info(f"Performed addition: {a} + {b} = {result}")
        return result

    def subtract(self, a, b):
        result = a - b
        self.update_history(f"{a} - {b}", result)
        logging.info(f"Performed subtraction: {a} - {b} = {result}")
        return result

    def multiply(self, a, b):
        result = a * b
        self.update_history(f"{a} * {b}", result)
        logging.info(f"Performed multiplication: {a} * {b} = {result}")
        return result

    def divide(self, a, b):
        if b == 0:
            logging.error("Attempted to divide by zero.")
            return "Division by zero!"
        result = a / b
        self.update_history(f"{a} / {b}", result)
        logging.info(f"Performed division: {a} / {b} = {result}")
        return result

    def update_history(self, expression, result):
        new_row = pd.DataFrame({'Expression': [expression], 'Result': [result]})
        self.history = pd.concat([self.history, new_row], ignore_index=True)
        self.save_history()

    def show_history(self):
        if not self.history.empty:
            logging.info("Displaying calculation history.")
            print(self.history)
        else:
            logging.warning("No calculation history available.")

    def save_history(self):
        try:
            self.history.to_csv(self.history_file, index=False)
            logging.info("History saved successfully.")
        except Exception as e:
            logging.error(f"Error saving history: {e}")

    def load_history(self):
        if os.path.exists(self.history_file):
            try:
                self.history = pd.read_csv(self.history_file)
                logging.info("History loaded successfully.")
            except Exception as e:
                logging.error(f"Error loading history: {e}")
                self.history = pd.DataFrame(columns=['Expression', 'Result'])
        else:
            logging.info("No saved history found. Starting with an empty history.")
            self.history = pd.DataFrame(columns=['Expression', 'Result'])
        return self.history

    def clear_history(self):
        self.history = pd.DataFrame(columns=['Expression', 'Result'])
        logging.info("History cleared.")

    def delete_history_file(self):
        if os.path.exists(self.history_file):
            try:
                os.remove(self.history_file)
                logging.info("History file deleted.")
            except Exception as e:
                logging.error(f"Error deleting history file: {e}")
        else:
            logging.warning("No history file to delete.")
