'''
Project 1: search

This project is about important theoretical and practical algorithms, rather than abstract
data types. Sorting and searching are at the heart of many ideas and algorithms in
Computing as a Science. This project will help train your intuition for algorithm
analysis and Big-O notation. Expected timing values assume that you implement good
versions of the algorithms.

'''

import math
import random
import time


def linear_search(nums, target) -> bool:
    for num in nums:
        if num == target:
            return True
    return False


def binary_search(nums, target) -> bool:
    left = 0
    right = len(nums)
    while left < right:
        pivot = (left + right) // 2
        if nums[pivot] == target:
            return True
        if nums[pivot] > target:
            right = pivot
        else:
            left = pivot + 1
    return False


def jump_search(nums, target) -> bool:
    jump_size = int(math.sqrt(len(nums)))
    position = 0

    while position < len(nums):
        if nums[position] == target:
            return True
        if nums[position] < target:
            position += jump_size
        elif position == 0:
            return False
        else:

            for index in range(1, jump_size):
                if nums[position - index] == target:
                    return True
            return False

    # jump back
    position -= (jump_size - 1)
    while position < len(nums):
        if nums[position] == target:
            return True
        position += 1

    return False


def time_function(run_search, nums, target):
    start = time.perf_counter()
    run_search(nums, target)
    f_time = time.perf_counter() - start
    return f_time


def print_results(nums, target):
    f_time = time_function(linear_search, nums, target)
    print("\tlinear_search: ", f_time)
    f_time = time_function(binary_search, nums, target)
    print("\tbinary_search: ", f_time)
    f_time = time_function(jump_search, nums, target)
    print("\tjump_search:   ", f_time)


def main():
    random.seed(1111)
    max_num = 100000000
    array_len = 10000000

    nums = sorted(random.sample(range(max_num), k=array_len))

    print("\nnumber at the start of the array:")
    target = nums[0]
    print_results(nums, target)

    print("\nnumber in the middle of the array:")
    target = nums[len(nums) // 2]
    print_results(nums, target)

    print("\nnumber at end of the array:")
    target = nums[len(nums) - 1]
    print_results(nums, target)

    print("\nnumber not in the array:")
    target = max_num + 1
    print_results(nums, target)
    print()


if __name__ == "__main__":
    main()
