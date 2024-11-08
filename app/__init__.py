import os
import pkgutil
import importlib
import sys
import logging
import logging.config
from dotenv import load_dotenv
from app.commands import CommandHandler, Command
from app.commands.history_command import HistoryCommand 
from app.core import Calculator  

class App:
    def __init__(self):
        os.makedirs('logs', exist_ok=True)
        self.configure_logging()
        load_dotenv()
        self.settings = self.load_environment_variables()
        self.settings.setdefault('ENVIRONMENT', 'PRODUCTION')
        self.command_handler = CommandHandler()
        self.calculator = Calculator() 

        self.command_handler.register_command("history", HistoryCommand(self.calculator))
        self.load_plugins()

    def configure_logging(self):
        logging_conf_path = 'logging.conf'
        if os.path.exists(logging_conf_path):
            logging.config.fileConfig(logging_conf_path, disable_existing_loggers=False)
        else:
            logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
        logging.info("Logging configured.")

    def load_environment_variables(self):
        settings = {key: value for key, value in os.environ.items()}
        logging.info("Environment variables loaded.")
        return settings

    def get_environment_variable(self, env_var: str = 'ENVIRONMENT'):
        return self.settings.get(env_var, None)

    def load_plugins(self):
        """Dynamically loads plugins from the plugins directory."""
        plugins_package = 'app.plugins'
        plugins_path = plugins_package.replace('.', '/')
        
        if not os.path.exists(plugins_path):
            logging.warning(f"Plugins directory '{plugins_path}' not found.")
            return
        
        for _, plugin_name, is_pkg in pkgutil.iter_modules([plugins_path]):
            if not is_pkg:
                try:
                    plugin_module = importlib.import_module(f'{plugins_package}.{plugin_name}')
                    self.register_plugin_commands(plugin_module, plugin_name)
                except ImportError as e:
                    logging.error(f"Error importing plugin '{plugin_name}': {e}")

    def register_plugin_commands(self, plugin_module, plugin_name):
        """Registers commands from plugins into the command handler."""
        for item_name in dir(plugin_module):
            item = getattr(plugin_module, item_name)
            if isinstance(item, type) and issubclass(item, Command) and item is not Command:
                command_instance = item()
                command_name = command_instance.__class__.__name__.replace("Command", "").lower()  # E.g., AddCommand -> add
                self.command_handler.register_command(command_name, command_instance)
                logging.info(f"Command '{command_name}' from plugin '{plugin_name}' registered.")

    def start(self):
        logging.info("Application started. Type 'exit' to exit.")
        try:
            while True:
                cmd_input = input(">>> ").strip()
                if cmd_input.lower() == 'exit':
                    logging.info("Application exit.")
                    sys.exit(0)  
                try:
                    self.command_handler.execute_command(cmd_input)
                except KeyError: 
                    logging.error(f"Unknown command: {cmd_input}")
        except KeyboardInterrupt:
            logging.info("Application interrupted and exiting gracefully.")
            sys.exit(0)  
        finally:
            logging.info("Application shutdown.")

if __name__ == "__main__":
    app = App()
    app.start()