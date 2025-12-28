#! /usr/bin/env python3


# TODO: find best combination of multiple troops, given that you can use each as many times as you want
# currenty you are limited to 6 times each troop OR 5 times first and 1 time second OR 4 times first and 2 times second AND SO ON

from argparse import ArgumentParser
from itertools import product

from troop import ALL_TROOPS, Troop, combine_troops

LIMIT_DIMINISHING_RETURNS = 0.02

LIMIT_CALC_STEPS = 7


def main() -> None:
    find_best_combination_of_troops_with_diferent_counts(ALL_TROOPS)
    # find_best_combination_of_multiple_troops(ALL_TROOPS)
    # find_best_combination_of_2_troops(ALL_TROOPS)
    # find_best_single_troop(ALL_TROOPS)

    # troop_tank = TANK * 2
    # print(f"{troop_tank=}")
    # troop = combine_troops([COMMANDO, ROCKET_ARTILLERY, troop_tank])
    # print(f"{troop=}")


def find_best_combination_of_troops_with_diferent_counts(
    all_troops: set[Troop],
) -> None:
    mixed_troops: set[Troop] = set()

    for counts in product(range(0, LIMIT_CALC_STEPS + 1), repeat=len(all_troops)):
        # print(f"{counts=}")

        multiplied_troops = [
            troop * count
            for troop, count in zip(all_troops, counts, strict=True)
            if count != 0
        ]

        if len(multiplied_troops) == 0:
            continue

        new_troop = combine_troops(multiplied_troops)

        ##### add new troop

        mixed_troops.add(new_troop)

    find_best_single_troop(mixed_troops)

    # mixed_troops: set[Troop] = set()

    # for combination in product(*([ALL_TROOPS] * len(ALL_TROOPS))):
    #     # print(f"{combination=}")
    #     new_troop = combine_troops(combination)

    #     do_add = True

    #     for registered_troop in mixed_troops:
    #         if registered_troop.name == new_troop.name:
    #             do_add = False

    #     if do_add:
    #         mixed_troops.add(new_troop)

    # find_best_single_troop(mixed_troops)


# def find_best_combination_of_multiple_troops(all_troops: set[Troop]) -> None:
#     mixed_troops: set[Troop] = set()

#     for combination in product(*([all_troops] * len(all_troops))):
#         # print(f"{combination=}")
#         new_troop = combine_troops(combination)

#         do_add = True

#         for registered_troop in mixed_troops:
#             if registered_troop.name == new_troop.name:
#                 do_add = False

#         if do_add:
#             mixed_troops.add(new_troop)

#     find_best_single_troop(mixed_troops)


# def find_best_combination_of_2_troops(all_troops_as_set: set[Troop]) -> None:
#     all_troops = list(all_troops_as_set)

#     mixed_troops: set[Troop] = set()

#     for troop_a_idx, troop_a in enumerate(all_troops):
#         for troop_b in all_troops[troop_a_idx:]:
#             new_troop = troop_a + troop_b
#             # print(f"{new_troop=}")
#             # print()
#             mixed_troops.add(new_troop)

#     find_best_single_troop(mixed_troops)


def find_best_single_troop(all_troops: set[Troop]) -> None:
    coefficients_as_dict: dict[Troop, float] = {}

    for troop in all_troops:
        ratio_defense = troop.defense / troop.attack
        ratio_pierce = troop.pierce / troop.attack

        diminishing_returns = abs(1 - ratio_defense) + abs(1 - ratio_pierce)
        if diminishing_returns > LIMIT_DIMINISHING_RETURNS:
            continue

        # power = troop.attack

        coefficients_as_dict[troop] = diminishing_returns * -1
        # coefficients_as_dict[troop] = power

        # print(f"{troop=}")
        # print()

    coefficients = list(coefficients_as_dict.items())
    # coefficients.sort(key=lambda i: i[1])
    coefficients.sort(key=lambda i: i[0].attack, reverse=True)

    for troop, goodness in reversed(coefficients):
        print(f"{goodness=:.4f}")
        print(f"{troop=}")
        print()


def run_from_cmdline() -> None:
    parser = ArgumentParser()
    _args = parser.parse_args()
    main()


if __name__ == "__main__":
    run_from_cmdline()
