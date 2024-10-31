from app.plugins.plugin import Plugin

class GreetPlugin(Plugin):
    def get_command_name(self):
        return "greet"

    def execute(self, name):
        return f"Hello, {name}!"
