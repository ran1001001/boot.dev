def remove_invalid_lines(document):
    return "\n".join(filter(lambda x: False if x.startswith("-") else True, document.split("\n")))


def test(document):
    print("Input:")
    print(document)
    print("-------------------------------------")
    print("Output:")
    print(remove_invalid_lines(document))
    print("=====================================")


def main():
    test(
        """# My Essay
* How we win
- How you lose
* Why you're bad
"""
    )
    test(
        """# The Plan
* Phase 1
- ???
- Profit
Any questions?
"""
    )


main()
