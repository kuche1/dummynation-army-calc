#! /usr/bin/env python3

from argparse import ArgumentParser

from troop import ALL_TROOPS, Troop

# LIMIT_RECRUITMENT_COST = 5_000_000


def main() -> None:
    # find_best_single_troop(ALL_TROOPS)
    find_best_combination_of_2_troops(ALL_TROOPS)


def find_best_combination_of_2_troops(all_troops_as_set: set[Troop]) -> None:
    all_troops = list(all_troops_as_set)

    mixed_troops: set[Troop] = set()

    for troop_a_idx, troop_a in enumerate(all_troops):
        for troop_b in all_troops[troop_a_idx:]:
            new_troop = troop_a + troop_b
            # print(f"{new_troop=}")
            # print()
            mixed_troops.add(new_troop)

    find_best_single_troop(mixed_troops)


def find_best_single_troop(all_troops: set[Troop]) -> None:
    coefficients_as_dict: dict[Troop, float] = {}

    for troop in all_troops:
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
