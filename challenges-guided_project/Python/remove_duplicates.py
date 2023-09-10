def remove_duplicates(spells):
    newSet = set()
    for spell in spells:
        newSet.add(spell)
    return list(newSet)


def main():
    final = remove_duplicates(
        [
            "fireball",
            "eldrich blast",
            "fireball",
            "eldrich blast",
            "water gun",
            "eldrich blast",
            "water gun",
            "water gun",
            "fireball",
            "fireball",
            "sunburst",
            "fireball",
            "fireball",
        ]
    )
    final.sort()
    print(final)


main()
