#!/usr/bin/env python3
"""A tiny hello world CLI."""

import argparse


def greet(name: str = "world") -> str:
    """Return a greeting for name, falling back to 'world' if blank."""
    name = name.strip()
    if not name:
        name = "world"
    return f"Hello, {name}!"


def main() -> None:
    parser = argparse.ArgumentParser(description="Print a friendly greeting.")
    parser.add_argument(
        "name",
        nargs="?",
        default="world",
        help="name to greet (default: world)",
    )
    parser.add_argument(
        "--upper",
        action="store_true",
        help="uppercase the whole greeting",
    )
    args = parser.parse_args()

    message = greet(args.name)
    if args.upper:
        message = message.upper()
    print(message)


if __name__ == "__main__":
    main()
