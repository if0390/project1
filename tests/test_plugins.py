import pytest
from app.plugins.example_plugin import ExamplePlugin

def test_greet():
    plugin = ExamplePlugin()
    assert plugin.execute("greet", "Alice") == "Hello, Alice!"

def test_menu():
    plugin = ExamplePlugin()
    assert plugin.execute("menu") == "Available commands: greet, menu"
