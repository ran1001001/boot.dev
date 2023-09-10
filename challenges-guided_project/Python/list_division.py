def divide_list(nums, divisor):
    result = []
    for num in nums:
        result.append(num / divisor)
    return result


def test(nums, divisor):
    res = divide_list(nums, divisor)
    print(f"given nums={nums} and divisor={divisor}, {res} was returned")


test([6, 8, 10], 2)
test([9, 21, 333312], 3)
test([5, 25, 543664565], 5)
