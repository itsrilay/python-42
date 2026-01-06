from ex4.TournamentCard import TournamentCard
from ex4.TournamentPlatform import TournamentPlatform


def main() -> None:
    print("\n=== DataDeck Tournament Platform ===")

    print("\nRegistering Tournament Cards...\n")
    cards = [
        TournamentCard("Fire Dragon", 5, "Legendary", 7, 5, 3, 1200),
        TournamentCard("Ice Wizard", 3, "Rare", 4, 3, 1, 1150)
    ]

    platform = TournamentPlatform()

    card_ids: list[str] = []

    for card in cards:
        info = card.get_card_info()
        rating_info = card.get_rank_info()

        wins, losses = rating_info["wins"], rating_info["losses"]

        card_id = platform.register_card(card)

        card_ids.append(card_id)

        parent_classes = [
            card.__name__
            for card in type(cards[0]).__mro__
            if card.__name__ not in [type(cards[0]).__name__, "object", "ABC"]
        ]

        print(f"{info['name']} (ID: {card_id}):")
        print(f"- Interfaces: [{', '.join(parent_classes)}]")
        print(f"- Rating: {card.get_rank_info()['rating']}")
        print(f"- Record: {wins}-{losses}\n")

    print("Creating tournament match...")
    card1_id, card2_id = card_ids[0], card_ids[1]
    print(f"Match result: {platform.create_match(card1_id, card2_id)}")

    print("\nTournament Leaderboard:")
    leaderboard = platform.get_leaderboard()

    i = 1
    for card in leaderboard:
        info = card.get_card_info()
        rating_info = card.get_rank_info()

        rating = rating_info["rating"]
        wins, losses = rating_info["wins"], rating_info["losses"]

        print(f"{i}. {info['name']} - Rating: {rating} ({wins}-{losses})")
        i += 1

    print("\nPlatform Report:")
    print(platform.generate_tournament_report())

    print("\n=== Tournament Platform Successfully Deployed! ===")
    print("All abstract patterns working together harmoniously!")


if __name__ == "__main__":
    main()
