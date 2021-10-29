# Tower of Hanoi

def tower_hanoi(n, s, a, d):
    if n == 1:
        print(f"move {n}st disk from {s} to {d}")
        return
    tower_hanoi(n-1, s, d, a)
    print(f"move {n} disk from {s} to {d}")
    tower_hanoi(n-1, a, s, d)


print(tower_hanoi(4, "source", "auxillary", "destination"))


