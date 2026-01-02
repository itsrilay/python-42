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
        attack_power: int,
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
            attack_power (int): The damage value dealt during attacks.
            health (int): The current hit points of the card.
            mana (int): The current mana pool available for casting spells.
            armor (int): Damage reduction value applied to incoming attacks.
            combat_type (str): The style of combat (e.g., 'melee', 'ranged').
        """
        super().__init__(name, cost, rarity)
        self.attack_power = attack_power
        self.health = health
        self.mana = mana
        self.armor = armor
        self.combat_type = combat_type

    def play(self, game_state: dict[str, Any]) -> dict[str, Any]:
        """
        Execute the action of playing the elite card.

        Args:
            game_state (dict[str, Any]): The current state of the game.

        Returns:
            dict[str, Any]: A result dictionary indicating the card was played.
        """
        return super().play(game_state)

    def attack(self, target: Combatable) -> dict[str, Any]:
        """
        Perform an attack on a target entity.

        Args:
            target (Combatable): The entity being attacked.

        Returns:
            dict[str, Any]: A dictionary detailing the attack, including
            attacker name, target name, damage dealt, and combat type.
        """
        target.defend(self.attack_power)
        target_name = getattr(target, "name", "Enemy")
        return {
            "attacker": self.name,
            "target": target_name,
            "damage": self.attack_power,
            "combat_type": self.combat_type
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
        taken = max(incoming_damage - self.armor, 0)
        self.health -= taken
        return {
            "defender": self.name,
            "damage_taken": taken,
            "damage_blocked": self.armor,
            "still_alive": self.health > 0
        }

    def get_combat_stats(self) -> dict[str, Any]:
        """
        Retrieve the card's combat-related statistics.

        Returns:
            dict[str, Any]: A dictionary containing health, attack, and armor.
        """
        return {
            "health": self.health,
            "attack": self.attack_power,
            "armor": self.armor
        }

    def cast_spell(
        self,
        spell_name: str,
        targets: list[Combatable]
    ) -> dict[str, Any]:
        """
        Cast a spell on a list of targets, consuming mana.

        Args:
            spell_name (str): The name of the spell.
            targets (list[Combatable]): The targets of the spell.

        Returns:
            dict[str, Any]: A dictionary detailing the spell cast, targets,
            and mana consumed.
        """
        tars = [getattr(t, "name", f"Enemy{i}") for i, t in enumerate(targets)]
        self.mana -= 4
        return {
            "caster": self.name,
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
        self.mana += amount
        return {
            "channeled": amount,
            "total_mana": self.mana
        }

    def get_magic_stats(self) -> dict[str, Any]:
        """
        Retrieve the card's magic-related statistics.

        Returns:
            dict[str, Any]: A dictionary containing the current mana.
        """
        return {"mana": self.mana}
