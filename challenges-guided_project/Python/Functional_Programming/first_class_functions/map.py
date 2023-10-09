def change_bullet_style(document):
    return "\n".join(map(convert_line, document.split("\n")))


def convert_line(line):
    old_bullet = "-"
    new_bullet = "*"
    if len(line) > 0 and line[0] == old_bullet:
        return new_bullet + line[1:]
    return line


def test(document):
    print("Input:")
    print(document)
    print("-------------------------------------")
    print("Output:")
    print(change_bullet_style(document))
    print("=====================================")


def main():
    test(
        """# My Essay
- How we win
- How you lose
- Why you're bad mega-person
"""
    )
    test(
        """# The Plan
- Phase 1
- ???
- Profit
Any questions?
"""
    )


main()
