import pandas as pd
import os

class Calculator:
    def __init__(self):
        self.history_file = "history.csv"
        self.history = self.load_history() 

    def add(self, a, b):
        result = a + b
        self.update_history(f"{a} + {b}", result)
        return result

    def subtract(self, a, b):
        result = a - b
        self.update_history(f"{a} - {b}", result)
        return result

    def multiply(self, a, b):
        result = a * b
        self.update_history(f"{a} * {b}", result)
        return result

    def divide(self, a, b):
        if b == 0:
            return "Division by zero!"
        result = a / b
        self.update_history(f"{a} / {b}", result)
        return result

    def update_history(self, expression, result):
        new_row = pd.DataFrame({'Expression': [expression], 'Result': [result]})
        self.history = pd.concat([self.history, new_row], ignore_index=True)
        self.save_history()

    def show_history(self):
        if not self.history.empty:
            print(self.history)
        else:
            print("No calculation history available.")

    def save_history(self):
        try:
            self.history.to_csv(self.history_file, index=False)
        except Exception as e:
            print(f"Error saving history: {e}")

    def load_history(self):
        if os.path.exists(self.history_file):
            try:
                history_data = pd.read_csv(self.history_file)
                print("History loaded successfully.")  
                return history_data
            except Exception as e:
                print(f"Error loading history: {e}")
                return pd.DataFrame(columns=['Expression', 'Result'])
        else:
            print("No saved history found. Starting with an empty history.")
            return pd.DataFrame(columns=['Expression', 'Result'])

    def clear_history(self):
        self.history = pd.DataFrame(columns=['Expression', 'Result'])
        self.save_history() 
        print("History cleared.")

    def delete_history_file(self):
        if os.path.exists(self.history_file):
            try:
                os.remove(self.history_file)
                print("History file deleted.")
            except Exception as e:
                print(f"Error deleting history file: {e}")
        else:
            print("No history file to delete.")

