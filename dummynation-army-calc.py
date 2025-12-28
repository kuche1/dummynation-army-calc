#! /usr/bin/env python3

from argparse import ArgumentParser

import troop

print(f"{troop.COMMANDO=}")


def main() -> None:
    pass


def run_from_cmdline() -> None:
    parser = ArgumentParser()
    _args = parser.parse_args()
    main()


if __name__ == "__main__":
    run_from_cmdline()
