'''
Project 2: sort

'''

import random
import time


def time_function(run_f, args):
    start = time.perf_counter()
    print(is_sorted(run_f(args)))
    f_time = time.perf_counter() - start
    return f_time


def print_results(nums):
    print("starting selection_sort")
    f_time = time_function(selection_sort, nums.copy())
    print(f"selection_sort duration: {f_time} seconds.")
    print("starting insertion_sort ")
    f_time = time_function(insertion_sort, nums.copy())
    print(f"insertion_sort duration: {f_time} seconds.")
    print("starting mergesort")
    f_time = time_function(mergesort, nums.copy())
    print(f"mergesort duration: {f_time} seconds.")
    print("starting quicksort")
    f_time = time_function(quicksort, nums.copy())
    print(f"quicksort duration: {f_time} seconds.")
    print("starting timsort ")
    f_time = time_function(timsort, nums.copy())
    print(f"timsort duration: {f_time} seconds.")


def main():
    random.seed(1111)
    max_num = 10000000
    array_len = 10000
    nums: list[int] = random.sample(range(max_num), k=array_len)
    print_results(nums)


def quicksort(nums: list[int]) -> list[int]:
    nums.sort()
    return nums


def mergesort(nums: list[int]) -> list[int]:
    nums.sort()
    return nums


def selection_sort(nums: list[int]) -> list[int]:
    for i in range(0, len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] > nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
    return nums


def insertion_sort(nums: list[int]) -> list[int]:
    for i in range(0, len(nums)):
        j = i
        while j > 0 and nums[j] < nums[j-1]:
            nums[j-1], nums[j] = nums[j], nums[j-1]
            j -= 1

    return nums


def timsort(nums: list[int]) -> list[int]:
    nums.sort()
    return nums


def is_sorted(nums) -> bool:
    if (all(nums[i] <= nums[i + 1] for i in range(len(nums) - 1))):
        return True
    return False


if __name__ == "__main__":
    main()
