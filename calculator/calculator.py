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
            print("History saved successfully.")
        except Exception as e:
            print(f"Error saving history: {e}")

    def load_history(self):
        """Load history from the file and update in-memory history."""
        if os.path.exists(self.history_file):
            try:
                self.history = pd.read_csv(self.history_file)  
                print("History loaded successfully.")  
            except Exception as e:
                print(f"Error loading history: {e}")
                self.history = pd.DataFrame(columns=['Expression', 'Result']) 
        else:
            print("No saved history found. Starting with an empty history.")
            self.history = pd.DataFrame(columns=['Expression', 'Result'])  
        return self.history

    def clear_history(self):
        """Clear in-memory history without saving the empty history to the file."""
        self.history = pd.DataFrame(columns=['Expression', 'Result'])
        print("History cleared.")

    def delete_history_file(self):
        """Delete the history file if it exists."""
        if os.path.exists(self.history_file):
            try:
                os.remove(self.history_file)
                print("History file deleted.")
            except Exception as e:
                print(f"Error deleting history file: {e}")
        else:
            print("No history file to delete.")