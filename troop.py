_K = 1_000
_M = _K * 1_000

_TARGET_MAINTNANCE_COST = 1 * _M


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
        multiplier = _TARGET_MAINTNANCE_COST / maintenance_cost

        self.military_personel = multiplier * military_personel
        self.recruitment_cost = multiplier * recruitment_cost
        self.maintenance_cost = multiplier * maintenance_cost

        self.attack = multiplier * attack
        self.defense = multiplier * defense
        self.pierce = multiplier * pierce

        self.speed = speed

    def __repr__(self) -> str:
        return f"Troop:\n    military_personel: {self.military_personel:_.1f}\n    recruitment_cost: {self.recruitment_cost:_.1f}\n    maintenance_cost: {self.maintenance_cost:_.1f}\n    attack: {self.attack:_.1f}\n    defense: {self.defense:_.1f}\n    pierce: {self.pierce:_.1f}\n    speed: {self.speed}"


COMMANDO = _Troop(
    1 * _K,
    6.35 * _K,
    403.73,
    15 * _K,
    5.55 * _K,
    4 * _K,
    10,
)

GUNNER = _Troop(
    1 * _K,
    9.49 * _K,
    603.68,
    12 * _K,
    2.22 * _K,
    19 * _K,
    8,
)

TANK = _Troop(
    70,
    14.2 * _K,
    140.86,
    7.7 * _K,
    19.42 * _K,
    3.5 * _K,
    5,
)

ROCKET_ARTILERY = _Troop(
    225,
    12.26 * _K,
    241.01,
    900,
    5.99 * _K,
    22.5 * _K,
    6,
)

HELICOPTER = _Troop(
    25,
    11.27 * _K,
    167.16,
    25 * _K,
    2.22 * _K,
    500,
    16,
)

COMBAT_AIRCRAFT = _Troop(
    4,
    12.12 * _K,
    106.98 * _K,
    6 * _K,
    11.1 * _K,
    8 * _K,
    20,
)

ALL_TROOPS = {COMMANDO, GUNNER, TANK, ROCKET_ARTILERY, HELICOPTER, COMBAT_AIRCRAFT}
