#! /usr/bin/env python3

from argparse import ArgumentParser

from troop import ALL_TROOPS, Troop

# LIMIT_RECRUITMENT_COST = 5_000_000


def main() -> None:
    coefficients_as_dict: dict[Troop, float] = {}

    for troop in ALL_TROOPS:
        ratio_defense = troop.defense / troop.attack
        ratio_pierce = troop.pierce / troop.attack

        badnesss = abs(1 - ratio_defense) + abs(1 - ratio_pierce)
        coefficients_as_dict[troop] = badnesss * -1

        # print(f"{troop=}")
        # print()

    coefficients = list(coefficients_as_dict.items())
    coefficients.sort(key=lambda i: i[1])

    for troop, goodness in coefficients:
        print(f"{goodness=:.2f}")
        print(f"{troop=}")
        print()


def run_from_cmdline() -> None:
    parser = ArgumentParser()
    _args = parser.parse_args()
    main()


if __name__ == "__main__":
    run_from_cmdline()
