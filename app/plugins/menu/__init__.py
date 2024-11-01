from app.plugins.plugin import Plugin

class MenuPlugin(Plugin):
    def get_command_name(self):
        return "menu"

    def execute(self):
        return "Available commands: greet, add, subtract, multiply, divide, greet, menu, history, clear, load, delete, quit"
