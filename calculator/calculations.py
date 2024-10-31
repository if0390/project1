import pandas as pd

class Calculations:
    history = pd.DataFrame(columns=["operation", "operand1", "operand2", "result"])

    @staticmethod
    def add_calculation(calculation):
        operation = calculation.operation.__name__
        operand1 = calculation.a
        operand2 = calculation.b
        result = calculation.perform()
        
        new_entry = pd.DataFrame({
            "operation": [operation],
            "operand1": [operand1],
            "operand2": [operand2],
            "result": [result]
        })

        Calculations.history = pd.concat([Calculations.history, new_entry], ignore_index=True)
        print("Added calculation to history:", operation, operand1, operand2, result)  # Debugging print

    @staticmethod
    def get_history():
        return Calculations.history

    @staticmethod
    def clear_history():
        Calculations.history = Calculations.history.iloc[0:0]  # Clears DataFrame