from app.plugins.plugin import Plugin

class ExamplePlugin(Plugin):
    def get_command_name(self):
        return "example"

    def execute(self, *args):
        if not args:
            return "This is an example plugin command!"
        command = args[0].lower()
        if command == "greet":
            return f"Hello, {args[1]}!" if len(args) > 1 else "Hello!"
        elif command == "menu":
            return "Available commands: greet, menu"
        return "Unknown command."

