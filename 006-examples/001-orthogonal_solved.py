ALLOWED = "NSEW"


def validate_path(path):
    for i in range(len(path)):
        if path[i] not in ALLOWED:
            return False

    return True


def step_delta(ch):
    match ch:
        case "N":
            return 0, 1
        case "S":
            return 0, -1
        case "E":
            return 1, 0
        case "W":
            return -1, 0
        case _:
            raise ValueError(f"Invalid direction: {ch}")


def final_position(path):
    x, y = 0, 0

    for ch in path:
        dx, dy = step_delta(ch)
        x += dx
        y += dy

    return x, y


def first_return_to_origin_step(path):
    x, y = 0, 0

    for step_idx in range(len(path)):
        dx, dy = step_delta(path[step_idx])
        x += dx
        y += dy

        if x == 0 and y == 0:
            return step_idx

    return -1


def longest_straight_run(path):
    n = len(path)

    if n == 0:
        return (0, -1, -1)

    best_len = 1
    best_start = 0

    i = 0
    while i < n:
        j = i + 1

        while j < n and path[j] == path[i]:
            j += 1

        length = j - i

        if length > best_len:
            best_len = length
            best_start = i

        i = j

    return (best_len, best_start, best_start + best_len - 1)


samples = [
    "NNEESWWWSENNN",
    "NS",
    "EEEWWN",
    "",
    "NAXS",
]

print()

print("Orthogonal paths analysis\n")

for path in samples:
    try:
        if not validate_path(path):
            raise ValueError(f"Invalid path: {path}")

        pos = final_position(path)
        first_return = first_return_to_origin_step(path)
        run_len, run_start, run_end = longest_straight_run(path)

        print("----")
        print(f"Path: {path}")
        print(f"Final position: {pos}")
        print(f"First return to origin step: {first_return}")
        print(
            f"Longest straight run: length={run_len}, start={run_start}, end={run_end}")
    except ValueError as e:
        print(f"Error: {e}")
