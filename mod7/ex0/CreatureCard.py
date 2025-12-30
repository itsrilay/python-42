from ex0.Card import Card


class CreatureCard(Card):
    def __init__(
            self,
            name: str,
            cost: int,
            rarity: str,
            attack: int,
            health: int
    ) -> None:
        super().__init__(name, cost, rarity)
        try:
            if attack <= 0 or health <= 0:
                raise ValueError("Invalid CreatureCard attributes.")
        except ValueError as e:
            print(e)
        self.attack = attack
        self.health = health
