#! /usr/bin/env python3

# TODO: add the ability to treat manpower as the bottleneck rather than money

from argparse import ArgumentParser
from itertools import product

from troop import ALL_TROOPS, Troop, combine_troops

LIMIT_POWER_RATIO = 0.1
# if the ratio def/atk or pie/atk is too far off, ignore troop

LIMIT_CALC_STEPS = 2

LIMIT_SPEED = 0
# ignore everything with speed lower than this


def main() -> None:
    print_troop_stats(ALL_TROOPS)
    # find_best_combination_of_troops_with_diferent_counts(ALL_TROOPS)

    # find_best_combination_of_multiple_troops(ALL_TROOPS)
    # find_best_combination_of_2_troops(ALL_TROOPS)
    # find_best_single_troop(ALL_TROOPS)

    # troop_tank = TANK * 2
    # print(f"{troop_tank=}")
    # troop = combine_troops([COMMANDO, ROCKET_ARTILLERY, troop_tank])
    # print(f"{troop=}")


########## with respect to recruitment cost:
#
### best single stats:
# attack -> commando
# defense -> tank
# pierce -> gunner
#
### best sum of stats:
# Commando: 1_933_070_866.1
# Gunner: 1_750_263_435.2
# Helicopter: 1_229_813_664.6
# RocketArtillery: 1_198_613_376.8
# Tank: 1_078_169_014.1
# CombatAircraft: 1_035_478_547.9
#
########## with respect to recruitment speed:
#
### best single stats:
# attack -> helicopter
# defense -> tank
# pierce -> rocket artilery
#
### best sum of stats:
# Tank -> 1_531_000_000.0
# RocketArtillery -> 1_469_500_000.0
# Helicopter -> 1_386_000_000.0
# CombatAircraft -> 1_255_000_000.0
# Gunner -> 830_500_000.0
# Commando -> 613_750_000.0
#
def print_troop_stats(
    all_troops_as_set: set[Troop],
) -> None:
    all_trops = list(all_troops_as_set)
    all_trops.sort(key=lambda t: t.defense, reverse=True)
    # all_trops.sort(key=lambda t: t.attack + t.defense + t.pierce, reverse=False)

    for troop in reversed(all_trops):
        print(f"Total: {troop.attack + troop.defense + troop.pierce:_.1f}")
        print(troop)
        print()
        # print(f"{troop.name}: {troop.attack + troop.defense + troop.pierce:_.1f}")


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


def find_best_single_troop(all_troops: set[Troop]) -> None:
    coefficients_as_dict: dict[Troop, tuple[float, float]] = {}

    for troop in all_troops:
        if troop.speed < LIMIT_SPEED:
            continue

        ratio_defense = troop.defense / troop.attack
        ratio_defense = abs(1 - ratio_defense)
        if ratio_defense > LIMIT_POWER_RATIO:
            continue

        ratio_pierce = troop.pierce / troop.attack
        ratio_pierce = abs(1 - ratio_pierce)
        if ratio_pierce > LIMIT_POWER_RATIO:
            continue

        # power = troop.attack

        coefficients_as_dict[troop] = (ratio_defense, ratio_pierce)
        # coefficients_as_dict[troop] = power

        # print(f"{troop=}")
        # print()

    coefficients = list(coefficients_as_dict.items())
    # coefficients.sort(key=lambda i: i[1])
    coefficients.sort(key=lambda i: i[0].attack, reverse=True)

    for troop, bad_power_ratios in reversed(coefficients):
        print("bad ratios: ", end="")
        print([f"{ratio:.4f}" for ratio in bad_power_ratios])
        print(f"{troop}")
        print()


def run_from_cmdline() -> None:
    parser = ArgumentParser()
    _args = parser.parse_args()
    main()


if __name__ == "__main__":
    run_from_cmdline()

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
