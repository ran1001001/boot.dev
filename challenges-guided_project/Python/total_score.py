def merge(dict1, dict2):
    merged = {}
    merged["first_half"] = dict1
    merged["second_half"] = dict2
    return merged


def total_score(score_dict):
    first_total = score_dict["first_half"]["first_quarter"] + score_dict["first_half"]["second_quarter"]
    second_total = score_dict["second_half"]["third_quarter"] + score_dict["second_half"]["fourth_quarter"]
    return first_total + second_total


def test(first_half, second_half):
    merged = merge(first_half, second_half)
    total = total_score(merged)
    print(f"The team scored {total} points")


test(
    {"first_quarter": 24, "second_quarter": 31},
    {"third_quarter": 29, "fourth_quarter": 40},
)

test(
    {"first_quarter": 25, "second_quarter": 2},
    {"third_quarter": 31, "fourth_quarter": 0},
)


test(
    {"first_quarter": 12, "second_quarter": 2},
    {"third_quarter": 32, "fourth_quarter": 87},
)
