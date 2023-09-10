def join_strings(strings):
    return ",".join(strings)


def test(strings):
    joined = join_strings(strings)
    print(f"joined: {joined}")


test(["hello", "world"])
test(["this", "list", "is", "so", "important"])
test(["ford", "ferrari", "tesla"])
test(["musk", "satya", "cook", "bezos"])
test(["dota", "sc2", "overwatch", "diablo", "mtg"])
