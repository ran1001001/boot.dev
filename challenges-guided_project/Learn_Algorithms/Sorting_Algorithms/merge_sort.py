import time
import random


def merge_sort(nums):
    if len(nums) <= 1:
        return nums
    div = len(nums)//2
    left = nums[:div]
    right = nums[div:]
    return merge(merge_sort(left), merge_sort(right))


def merge(first, second):
    result = []

    while (len(first) > 0 and len(second) > 0):
        if first[0] > second[0]:
            result.append(second.pop(0))
        else:
            result.append(first.pop(0))

    # first or second is empty
    while (len(first) > 0):
        result.append(first.pop(0))

    while (len(second) > 0):
        result.append(second.pop(0))

    return result


def benchmark(nums, show_nums):
    start = time.time()
    test(nums, show_nums)
    end = time.time()

    timeout = 1.00

    if (end - start) < timeout:
        print(f"test completed in less than {timeout * 1000} milliseconds!")
    else:
        print(f"""test took too long ({(end - start) * 1000} milliseconds).
              Speed it up!""")
    print("====================================")


def test(nums, show_nums):
    res = merge_sort(nums.copy())
    if show_nums:
        print(f"nums: {nums}")
        print(f"sorted: {res}")
    else:
        print(f"len nums: {len(nums)}")
        print(f"len sorted: {len(res)}")
    print("------------------------------------")


def main():
    benchmark(get_nums(10), True)
    benchmark(get_nums(100), True)
    # benchmark(get_nums(1000), False)
    # benchmark(get_nums(10000), False)


def get_nums(num):
    nums = []
    random.seed(1)
    for i in range(num):
        nums.append(random.randint(0, len(nums)))
    return nums


main()
