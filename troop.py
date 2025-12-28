class _Troop:
    def __init__(
        self,
        military_personel: float,
        recruitment_cost: float,
        maintenance_cost: float,
        attack: float,
        defense: float,
        pierce: float,
        speed: int,
    ) -> None:
        self.military_personel = military_personel
        self.recruitment_cost = recruitment_cost
        self.maintenance_cost = maintenance_cost


k = 1_000
m = k * 1_000

COMMANDO = _Troop(
    1 * k,
    6.35 * k,
    403.73,
    15 * k,
    5.55 * k,
    4 * k,
    10,
)

GUNNER = _Troop(
    1 * k,
    9.49 * k,
    603.68,
    12 * k,
    2.22 * k,
    19 * k,
    8,
)

TANK = _Troop(
    70,
    14.2 * k,
    140.86,
    7.7 * k,
    19.42 * k,
    3.5 * k,
    5,
)

ROCKET_ARTILERY = _Troop(
    225,
    12.26 * k,
    241.01,
    900,
    5.99 * k,
    22.5 * k,
    6,
)

HELICOPTER = _Troop(
    25,
    11.27 * k,
    167.16,
    25 * k,
    2.22 * k,
    500,
    16,
)

COMBAT_AIRCRAFT = _Troop(
    4,
    12.12 * k,
    106.98 * k,
    6 * k,
    11.1 * k,
    8 * k,
    20,
)
