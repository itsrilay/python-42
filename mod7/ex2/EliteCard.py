"""
This module implements the EliteCard class for the DataDeck game.

It demonstrates multiple inheritance by combining Card, Combatable, and
Magical interfaces to create a complex, multi-functional game entity.
"""

from typing import Any
from ex0.Card import Card
from ex2.Combatable import Combatable
from ex2.Magical import Magical


class EliteCard(Card, Combatable, Magical):
    """
    A concrete implementation representing a powerful 'Elite' card.

    This class inherits from Card (identity), Combatable (fighting capability),
    and Magical (spellcasting capability), requiring implementation of all
    abstract methods from these three parents.
    """

    def __init__(
        self,
        name: str,
        cost: int,
        rarity: str,
        attack: int,
        health: int,
        mana: int,
        armor: int,
        combat_type: str
    ) -> None:
        """
        Initialize a new EliteCard instance.

        Args:
            name (str): The name of the card.
            cost (int): The mana cost to play the card.
            rarity (str): The rarity level of the card.
            attack (int): The damage value dealt during attacks.
            health (int): The current hit points of the card.
            mana (int): The current mana pool available for casting spells.
            armor (int): Damage reduction value applied to incoming attacks.
            combat_type (str): The style of combat (e.g., 'melee', 'ranged').
        """
        super().__init__(name, cost, rarity)
        self._attack = attack
        self._health = health
        self._mana = mana
        self._armor = armor
        self._combat_type = combat_type

    def play(self, game_state: dict[str, Any]) -> dict[str, Any]:
        """
        Execute the action of playing the elite card.

        Args:
            game_state (dict[str, Any]): The current state of the game.

        Returns:
            dict[str, Any]: A result dictionary indicating the card was played.
        """
        return super().play(game_state)

    def attack(self, target: Any) -> dict[str, Any]:
        """
        Perform an attack on a target entity.

        Args:
            target (Any): The entity being attacked.

        Returns:
            dict[str, Any]: A dictionary detailing the attack, including
            attacker name, target name, damage dealt, and combat type.
        """
        if hasattr(target, "defend"):
            damage_dealt = target.defend(self._attack)["damage_taken"]
        else:
            return {"error": "Invalid target"}

        return {
            "attacker": self._name,
            "target": target.get_card_info()["name"],
            "damage": damage_dealt,
            "combat_type": self._combat_type
        }

    def defend(self, incoming_damage: int) -> dict[str, Any]:
        """
        Process incoming damage, applying armor reduction.

        Args:
            incoming_damage (int): The raw damage amount received.

        Returns:
            dict[str, Any]: A dictionary detailing the defense, including
            actual damage taken, blocked amount, and survival status.
        """
        taken = max(incoming_damage - self._armor, 0)
        self._health -= taken
        return {
            "defender": self._name,
            "damage_taken": taken,
            "damage_blocked": self._armor,
            "still_alive": self._health > 0
        }

    def get_combat_stats(self) -> dict[str, Any]:
        """
        Retrieve the card's combat-related statistics.

        Returns:
            dict[str, Any]: A dictionary containing health, attack, and armor.
        """
        return {
            "health": self._health,
            "attack": self._attack,
            "armor": self._armor
        }

    def cast_spell(
        self,
        spell_name: str,
        targets: list[Any]
    ) -> dict[str, Any]:
        """
        Cast a spell on a list of targets, consuming mana.
        """

        tars: list[str] = []
        for i, t in enumerate(targets):
            if hasattr(t, "get_card_info"):
                tars.append(t.get_card_info()["name"])
            else:
                tars.append(getattr(t, "name", f"Enemy{i}"))

        self._mana -= 4

        return {
            "caster": self._name,
            "spell": spell_name,
            "targets": tars,
            "mana_used": 4
        }

    def channel_mana(self, amount: int) -> dict[str, Any]:
        """
        Add mana to the card's pool.

        Args:
            amount (int): The amount of mana to gain.

        Returns:
            dict[str, Any]: A dictionary showing the amount channeled and
            the new total mana.
        """
        self._mana += amount
        return {
            "channeled": amount,
            "total_mana": self._mana
        }

    def get_magic_stats(self) -> dict[str, Any]:
        """
        Retrieve the card's magic-related statistics.

        Returns:
            dict[str, Any]: A dictionary containing the current mana.
        """
        return {"mana": self._mana}
