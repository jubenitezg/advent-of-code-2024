def load() -> str:
    with open("day03/input.txt", "r", encoding="utf-8") as f:
        r = ""
        for line in f:
            r += line
        return r
