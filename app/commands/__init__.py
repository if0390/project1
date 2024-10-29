import logging

class Command:
    def execute(self, *args):
        raise NotImplementedError("Commands must implement the execute method.")

class CommandHandler:
    def __init__(self):
        self.commands = {}

    def register_command(self, name, command):
        """Registers a command with a specified name."""
        self.commands[name] = command
        logging.info(f"Registered command: {name}")

    def execute_command(self, input_str):
        """Executes a command based on the input string."""
        parts = input_str.split()
        cmd_name, args = parts[0], parts[1:]
        
        if cmd_name in self.commands:
            command = self.commands[cmd_name]
            command.execute(*args)
        else:
            raise KeyError(f"No such command: {cmd_name}")