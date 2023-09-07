def test_score(answer_sheet, student_answers):
    correct = 0
    name = student_answers[0]
    for i in range(0, len(answer_sheet)):  # i == 0-19
        if student_answers[i + 1] == answer_sheet[i]:
            correct += 1
    percentage = correct / len(answer_sheet)
    return name, percentage


def test(answer_sheet, student_1_answers):
    name, percentage = test_score(answer_sheet, student_1_answers)
    print(f"{name}: {percentage:.1f}%")


def main():
    answer_sheet = [
        "A",
        "A",
        "C",
        "D",
        "D",
        "B",
        "C",
        "A",
        "C",
        "B",
        "A",
        "D",
        "C",
        "B",
        "D",
        "C",
        "B",
        "A",
        "D",
        "A",
    ]
    student_1_answers = [  # testing score 17/20, percentage should be 80% for Allan
        "Allan",
        "A",  # A
        "C",  # A x
        "C",  # C
        "B",  # D x
        "D",  # D
        "B",  # B
        "C",  # C
        "A",  # A
        "C",  # C
        "B",  # B
        "A",  # A
        "A",  # D x
        "C",  # C
        "B",  # B
        "D",  # D
        "C",  # C
        "B",  # B
        "A",  # A
        "D",  # D
        "A",  # A
    ]
    student_2_answers = [
        "John",
        "A",
        "D",
        "A",
        "A",
        "D",
        "A",
        "C",
        "B",
        "D",
        "A",
        "F",
        "A",
        "C",
        "B",
        "D",
        "C",
        "D",
        "C",
        "D",
        "A",
    ]
    student_3_answers = [
        "Jeremy",
        "A",
        "B",
        "D",
        "C",
        "D",
        "B",
        "D",
        "A",
        "C",
        "C",
        "D",
        "A",
        "C",
        "B",
        "D",
        "C",
        "B",
        "A",
        "F",
        "A",
    ]
    student_4_answers = [
        "Sally",
        "A",
        "A",
        "D",
        "A",
        "A",
        "B",
        "C",
        "A",
        "C",
        "B",
        "A",
        "A",
        "C",
        "B",
        "D",
        "C",
        "F",
        "A",
        "D",
        "A",
    ]
    student_5_answers = [
        "Tim",
        "A",
        "A",
        "C",
        "D",
        "D",
        "B",
        "C",
        "A",
        "C",
        "B",
        "A",
        "D",
        "C",
        "B",
        "D",
        "C",
        "B",
        "A",
        "D",
        "A",
    ]

    test(answer_sheet, student_1_answers)
    test(answer_sheet, student_2_answers)
    test(answer_sheet, student_3_answers)
    test(answer_sheet, student_4_answers)
    test(answer_sheet, student_5_answers)


main()
