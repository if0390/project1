from app.plugins.plugin import Plugin

class MenuPlugin(Plugin):
    def get_command_name(self):
        return "menu"

    def execute(self):
        return "Available commands: greet, add, subtract, multiply, divide, history."
