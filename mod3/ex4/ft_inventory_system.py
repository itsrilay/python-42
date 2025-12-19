#!/usr/bin/env python3

def print_inventory(inventory: dict[str, dict[str, str | int]]) -> None:
    """
    Calculates total inventory value and item count.
    Constructs category str.

    Displays inventory value, item count and categories.
    """
    total_value = 0
    total_count = 0
    total_categories = {}

    for name, data in inventory.items():
        total_value += data["qty"] * data["price"]
        total_count += data["qty"]

        if data["type"] in total_categories:
            total_categories[data["type"]] += data["qty"]
        else:
            total_categories[data["type"]] = data["qty"]

        print(
            f"{name} ({data['type']}, {data['rarity']}):",
            f"{data['qty']}x @ {data['price']} gold each =",
            f"{data['qty'] * data['price']} gold"
        )

    final_str = ""
    i = 0
    for category, qty in total_categories.items():
        if i > 0:
            final_str += ", "
        final_str += f"{category} ({qty})"
        i += 1

    print(f"Inventory value: {total_value}")
    print(f"Item count: {total_count}")
    print(f"Categories: {final_str}")


def transfer_item(source, target, item_name, quantity) -> None:
    """
    Transfers item from source to target inventory.
    """
    if item_name in source:
        if source[item_name]["qty"] >= quantity:
            if item_name in target:
                target[item_name]["qty"] += quantity
            else:
                target[item_name] = {
                    "type": source[item_name]["type"],
                    "rarity": source[item_name]["rarity"],
                    "qty": quantity,
                    "price": source[item_name]["price"],
                }
            source[item_name]["qty"] -= quantity


def calc_value(inventory: dict[str, dict[str, str | int]]) -> int:
    """
    Calculates inventory value.

    Returns total value.
    """
    total_value = 0
    for data in inventory.values():
        total_value += data["qty"] * data["price"]
    return total_value


def calc_qty(inventory: dict[str, dict[str, str | int]]) -> int:
    """
    Calculates quantity of items in inventory.

    Returns total quantity.
    """
    total_qty = 0
    for data in inventory.values():
        total_qty += data["qty"]
    return total_qty


def get_rare_items(inventory: dict[str, dict[str, str | int]]) -> list[str]:
    """
    Retrieves rare items from inventory.

    Returns list with item names.
    """
    rare_list = []
    for name, data in inventory.items():
        if data["rarity"] == "rare":
            rare_list += [name]
    return rare_list


def print_analytics(
        alice_inventory: dict[str, dict[str, str | int]],
        bob_inventory: dict[str, dict[str, str | int]]) -> None:
    """
    Calculates and displays inventory analytics for Alice and Bob.
    """
    alice_gold = calc_value(alice_inventory)
    bob_gold = calc_value(bob_inventory)

    if alice_gold > bob_gold:
        mvp = "Alice"
        mvp_value = alice_gold
    else:
        mvp = "Bob"
        mvp_value = bob_gold

    alice_qty = calc_qty(alice_inventory)
    bob_qty = calc_qty(bob_inventory)

    if alice_qty > bob_qty:
        most_items = "Alice"
        most_items_qty = alice_qty
    else:
        most_items = "Bob"
        most_items_qty = bob_qty

    alice_rare = get_rare_items(alice_inventory)
    bob_rare = get_rare_items(bob_inventory)

    rare_items = alice_rare + bob_rare

    rare_str = ""
    i = 0
    while i < len(rare_items):
        rare_str += rare_items[i]
        if i < len(rare_items) - 1:
            rare_str += ", "
        i += 1

    print(f"Most valuable player: {mvp} ({mvp_value} gold)")
    print(f"Most items: {most_items} ({most_items_qty} items)")
    print(f"Rarest items: {rare_str}")


def main() -> None:
    """
    Orchestrates the calculation and display of all inventory operations.
    """
    print("=== Player Inventory System ===\n")

    print("=== Alice's Inventory ===")
    alice_inventory: dict[str, dict[str, str | int]] = {
        "sword": {
            "type": "weapon",
            "rarity": "rare",
            "qty": 1,
            "price": 500
        },
        "potion": {
            "type": "consumable",
            "rarity": "common",
            "qty": 5,
            "price": 50
        },
        "shield": {
            "type": "armor",
            "rarity": "uncommon",
            "qty": 1,
            "price": 200
        }
    }

    print_inventory(alice_inventory)

    print("\n=== Transaction: Alice gives Bob 2 potions ===")
    bob_inventory: dict[str, dict[str, str | int]] = {
        "magic_ring": {
            "type": "accessory",
            "rarity": "rare",
            "qty": 1,
            "price": 400
        }
    }

    transfer_item(alice_inventory, bob_inventory, "potion", 2)

    print("Transaction successful!")

    print("\n=== Updated Inventories ===")
    print(f"Alice potions: {alice_inventory['potion']['qty']}")
    print(f"Bob potions: {bob_inventory['potion']['qty']}")

    print("\n=== Inventory Analytics ===")

    print_analytics(alice_inventory, bob_inventory)


if __name__ == "__main__":
    main()
