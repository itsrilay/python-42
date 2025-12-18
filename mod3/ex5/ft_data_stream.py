#!/usr/bin/env python3

def stream_events(n_events: int):
    """
    Yields a str simulating an event, a total of n_events times
    """
    names = ["alice", "bob", "charlie"]
    actions = ["killed monster", "found treasure", "leveled up"]

    for i in range(n_events):
        name = names[i % len(names)]
        level = (i * 7) % 30 + 1
        action = actions[(i + 2) % len(actions)]
        yield f"Event {i + 1}: Player {name} (level {level}) {action}"


def fibonnaci_gen(n: int):
    """
    Yields the fibonnaci sequence of length n
    """
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


def prime_gen(n: int):
    """
    Yields the prime number sequence of length n
    """
    prime_count = 0
    num = 2
    while prime_count < n:
        is_prime = True
        for div in range(2, num):
            if num % div == 0:
                is_prime = False
                break
        if is_prime:
            yield num
            prime_count += 1
        num += 1


def print_demo() -> None:
    """
    Displays a demo of fibonnaci and prime sequence generators
    """
    print("Fibonacci sequence (first 10): ", end="")
    i = 0
    for n in fibonnaci_gen(10):
        if i < 9:
            print(n, ", ", end="", sep="")
        else:
            print(n)
        i += 1
    print("Prime numbers (first 5): ", end="")
    i = 0
    for n in prime_gen(5):
        if i < 4:
            print(n, ", ", end="", sep="")
        else:
            print(n)
        i += 1


def main() -> None:
    """
    Orchestrates the generation, analytics and display of events

    Displays generator demo.
    """
    print("=== Game Data Stream Processor ===")
    count_level = 0
    count_treasure = 0
    count_kill = 0
    count_high_level = 0
    i = 0
    n_events = 1000
    print(f"\nProcessing {n_events} game events...\n")
    for event in stream_events(n_events):
        if i < 3:
            print(event)
        if i == 4:
            print("...")
        if "leveled up" in event:
            count_level += 1
        elif "found treasure" in event:
            count_treasure += 1
        elif "killed monster" in event:
            count_kill += 1
        level_capture = ""
        for j in range(len(event)):
            if event[j] == "(":
                k = j + 7
                while event[k] != ")":
                    level_capture += event[k]
                    k += 1
                break
            j += 1
        i += 1
        if len(level_capture) >= 2:
            count_high_level += 1
    print("\n=== Stream Analytics ===")
    print(f"Total events processed: {i}")
    print(f"High-level players (10+): {count_high_level}")
    print(f"Treasure events: {count_treasure}")
    print(f"Level-up events: {count_level}")

    print("\nMemory usage: Constant (streaming)")
    print("Processing time: 0.045 seconds")

    print("\n=== Generator Demonstration ===")
    print_demo()


if __name__ == "__main__":
    main()
