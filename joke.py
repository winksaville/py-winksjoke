#!/usr/bin/env python3
from __future__ import annotations # Required for typing annotations

def hello(s: str) -> None:
    print(s)

if __name__ == "__main__":
    import sys
    import unittest
    from io import StringIO
    from unittest.mock import patch

    class TestHello(unittest.TestCase):
        def test_hello1(self: TestHello) -> None:
            with patch('sys.stdout', new=StringIO()) as capturedOutput:
                hello('wink')
            self.assertEqual(capturedOutput.getvalue().strip(), 'wink')

        def test_hello2(self: TestHello) -> None:
            with patch('sys.stdout', new=StringIO()) as capturedOutput:
                hello('wink saville')
            self.assertEqual(capturedOutput.getvalue().strip(), 'wink saville')

    unittest.main()
