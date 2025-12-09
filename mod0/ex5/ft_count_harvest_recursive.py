def ft_count_harvest_recursive(curr: int = 1, days: int | None = None) -> None:
    if days is None:
        days = int(input("Days until harvest: "))
    if curr <= days:
        print(f"Day {curr}")
        ft_count_harvest_recursive(curr + 1, days)
    else:
        print("Harvest time!")
