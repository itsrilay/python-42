def ft_harvest_total() -> None:
    total = 0
    i = 1
    while (i < 4):
        weight = int(input(f"Day {i} harvest: "))
        total += weight
        i += 1
    print(f"Total harvest: {total}")
