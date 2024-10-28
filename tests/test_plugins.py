from app.plugins.example_plugin import ExamplePlugin

def test_square():
    plugin = ExamplePlugin()
    assert plugin.square(3) == 9

def test_cube():
    plugin = ExamplePlugin()
    assert plugin.cube(2) == 8