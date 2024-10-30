import pytest
from app.repl import REPL  
from unittest.mock import patch

def test_repl_quit():
    repl = REPL()
    with patch("builtins.input", side_effect=["quit"]), patch("builtins.print") as mock_print:
        repl.start()
        mock_print.assert_any_call("Exiting calculator.")