from abc import ABC, abstractmethod

class Plugin(ABC):
    @abstractmethod
    def get_command_name(self):
        pass

    @abstractmethod
    def execute(self, *args):
        pass
