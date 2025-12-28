_K = 1_000
_M = _K * 1_000

_TARGET_RECRUITMENT_COST = 500_000 * _K


class Troop:
    def __init__(
        self,
        name: str,
        military_personel: float,
        recruitment_cost: float,
        maintenance_cost: float,
        attack: float,
        defense: float,
        pierce: float,
        speed: int,
        do_not_apply_multiplier: bool = False,
    ) -> None:
        if do_not_apply_multiplier:
            multiplier = 1
        else:
            multiplier = _TARGET_RECRUITMENT_COST / recruitment_cost

        self.name = name

        self.military_personel = multiplier * military_personel
        self.recruitment_cost = multiplier * recruitment_cost
        self.maintenance_cost = multiplier * maintenance_cost

        self.attack = multiplier * attack
        self.defense = multiplier * defense
        self.pierce = multiplier * pierce

        self.speed = speed

    def __repr__(self) -> str:
        return f"{self.name}:\n    military_personel: {self.military_personel:_.1f}\n    recruitment_cost: {self.recruitment_cost:_.1f}\n    maintenance_cost: {self.maintenance_cost:_.1f}\n    attack: {self.attack:_.1f}\n    defense: {self.defense:_.1f}\n    pierce: {self.pierce:_.1f}\n    speed: {self.speed}"

    # def __add__(self, other: "Troop") -> "Troop":
    #     # this is only good enough for adding 2 troops together, not 3 or more
    #     if self.name < other.name:
    #         name = f"{self.name} + {other.name}"
    #     else:
    #         name = f"{other.name} + {self.name}"

    #     return Troop(
    #         name,
    #         (self.military_personel + other.military_personel) / 2,
    #         (self.recruitment_cost + other.recruitment_cost) / 2,
    #         (self.maintenance_cost + other.maintenance_cost) / 2,
    #         (self.attack + other.attack) / 2,
    #         (self.defense + other.defense) / 2,
    #         (self.pierce + other.pierce) / 2,
    #         min(self.speed, other.speed),
    #     )

    def __mul__(self, multiplier: float) -> "Troop":
        return Troop(
            f"{self.name}*{multiplier}",
            self.military_personel * multiplier,
            self.recruitment_cost * multiplier,
            self.maintenance_cost * multiplier,
            self.attack * multiplier,
            self.defense * multiplier,
            self.pierce * multiplier,
            self.speed,
            do_not_apply_multiplier=True,
        )


COMMANDO = Troop(
    "Commando",
    1 * _K,
    6.35 * _K,
    403.73,
    15 * _K,
    5.55 * _K,
    4 * _K,
    10,
)

GUNNER = Troop(
    "Gunner",
    1 * _K,
    9.49 * _K,
    603.68,
    12 * _K,
    2.22 * _K,
    19 * _K,
    8,
)

TANK = Troop(
    "Tank",
    70,
    14.2 * _K,
    140.86,
    7.7 * _K,
    19.42 * _K,
    3.5 * _K,
    5,
)

ROCKET_ARTILLERY = Troop(
    "RocketArtillery",
    225,
    12.26 * _K,
    241.01,
    900,
    5.99 * _K,
    22.5 * _K,
    6,
)

HELICOPTER = Troop(
    "Helicopter",
    25,
    11.27 * _K,
    167.16,
    25 * _K,
    2.22 * _K,
    500,
    16,
)

COMBAT_AIRCRAFT = Troop(
    "CombatAircraft",
    4,
    12.12 * _K,
    106.98 * _K,
    6 * _K,
    11.1 * _K,
    8 * _K,
    20,
)

ALL_TROOPS = {COMMANDO, GUNNER, TANK, ROCKET_ARTILLERY, HELICOPTER, COMBAT_AIRCRAFT}


def combine_troops(troops: tuple[Troop, ...] | list[Troop]) -> Troop:
    all_names = [troop.name for troop in troops]
    all_names.sort()
    name = " + ".join(all_names)

    return Troop(
        name,
        sum([troop.military_personel for troop in troops]) / len(troops),
        sum([troop.recruitment_cost for troop in troops]) / len(troops),
        sum([troop.maintenance_cost for troop in troops]) / len(troops),
        sum([troop.attack for troop in troops]) / len(troops),
        sum([troop.defense for troop in troops]) / len(troops),
        sum([troop.pierce for troop in troops]) / len(troops),
        min([troop.speed for troop in troops]),
    )
