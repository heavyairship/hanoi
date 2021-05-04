state = {
    "A": [],
    "B": [],
    "C": []
}


def print_state():
    assert len(state["A"]) == len(state["B"]) == len(state["C"])

    print()

    def helper(e):
        return " " if e is None else str(e)

    for row in zip(state["A"], state["B"], state["C"]):
        print(" " + helper(row[0]) + "\t " +
              helper(row[1]) + "\t " + helper(row[2]))

    print("===\t===\t===")
    print(" A\t B\t C")
    print()


def move(dsc, src, dst):
    print("Moving from %d from %s to %s..." % (dsc, src, dst))

    state[src][state[src].index(dsc)] = None

    try:
        idx = state[dst].index(
            next(filter(lambda d: d is not None, state[dst])))
    except StopIteration:
        idx = len(state[dst])

    state[dst][idx-1] = dsc

    print_state()


def move_via(n, src, via, dst):
    if n == 0:
        return
    move_via(n-1, src, dst, via)
    move(n, src, dst)
    move_via(n-1, via, src, dst)


def solve(n):
    initialize(n)
    move_via(n, "A", "B", "C")


def initialize(n):
    r = range(1, n+1)
    state["A"] = [i for i in r]
    state["B"] = [None for i in r]
    state["C"] = [None for i in r]
    print()
    print("Initial state...")
    print_state()


while True:
    user_input = (input("enter a number of discs (q) to quit: "))
    if user_input in ["q", "Q"]:
        break
    solve(int(user_input))
