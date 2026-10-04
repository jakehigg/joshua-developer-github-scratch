"""Tests for hello.py."""

import subprocess
import sys
import unittest

from hello import greet


class GreetTests(unittest.TestCase):
    def test_default_greeting(self):
        self.assertEqual(greet(), "Hello, world!")

    def test_named_greeting(self):
        self.assertEqual(greet("Jake"), "Hello, Jake!")

    def test_empty_name_falls_back_to_world(self):
        self.assertEqual(greet(""), "Hello, world!")

    def test_whitespace_only_name_falls_back_to_world(self):
        self.assertEqual(greet("   "), "Hello, world!")

    def test_surrounding_whitespace_is_stripped(self):
        self.assertEqual(greet("  Jake  "), "Hello, Jake!")


class CliTests(unittest.TestCase):
    def run_cli(self, *args):
        return subprocess.run(
            [sys.executable, "hello.py", *args],
            capture_output=True,
            text=True,
            check=True,
        )

    def test_cli_default(self):
        result = self.run_cli()
        self.assertEqual(result.stdout.strip(), "Hello, world!")
        self.assertEqual(result.returncode, 0)

    def test_cli_named(self):
        result = self.run_cli("Jake")
        self.assertEqual(result.stdout.strip(), "Hello, Jake!")
        self.assertEqual(result.returncode, 0)

    def test_cli_upper(self):
        result = self.run_cli("Jake", "--upper")
        self.assertEqual(result.stdout.strip(), "HELLO, JAKE!")
        self.assertEqual(result.returncode, 0)


if __name__ == "__main__":
    unittest.main()
