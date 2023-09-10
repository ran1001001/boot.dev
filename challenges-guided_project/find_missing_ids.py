def find_missing_ids(first_ids, second_ids):
    return [id for id in first_ids if id not in second_ids]


def test(first_ids, second_ids):
    ids = sorted(find_missing_ids(first_ids, second_ids))
    print(f"Customers with these ids were only in the first list:")
    for id in ids:
        print(f"- {id}")
    print("---")


test([1, 1, 1, 2, 2, 2, 3], [1, 2])
test([1, 2, 2, 3, 4, 3, 4, 5, 6, 7, 8, 9, 9, 10], [1, 2, 2, 3, 4, 5, 6, 7, 8])
test(
    [1, 2, 2, 3, 4, 3, 4, 5, 6, 7, 8, 9, 9, 10, 11, 12, 13, 15, 18],
    [1, 2, 2, 3, 4, 5, 6, 7, 8, 100, 101, 103],
)
