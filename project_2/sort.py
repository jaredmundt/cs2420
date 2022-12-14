'''
Project 2: sort

'''

import random
import time


def main():
    random.seed(111)
    max_num = 1000000
    array_len = 10000
    nums: list[int] = random.sample(range(max_num), k=array_len)
    print_results(nums)


def time_function(run_f, args):
    start = time.perf_counter()
    run_f(args)
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


def quicksort(nums: list[int]) -> list[int]:

    def quicksort_helper(left, right, nums):

        if left < right:
            part = partition(left, right, nums)
            quicksort_helper(left, part - 1, nums)
            quicksort_helper(part + 1, right, nums)

    def partition(left, right, nums) -> int:

        index = left
        pivot = nums[right]

        for i in range(left, right):
            if nums[i] <= pivot:
                nums[i], nums[index] = nums[index], nums[i]
                index += 1
        nums[right], nums[index] = nums[index], nums[right]
        return index

    quicksort_helper(0, len(nums) - 1, nums)
    return nums


def mergesort(nums: list[int]) -> list[int]:

    def mergesort_helper(nums: list[int]) -> list[int]:
        if len(nums) < 2:
            return nums
        half = len(nums) // 2
        return merge(mergesort_helper(
            nums[:half]), mergesort_helper(nums[half:]))

    def merge(nums1: list[int], nums2: list[int]) -> list[int]:
        res: list[int] = []
        i = 0
        j = 0

        while i < len(nums1) or j < len(nums2):
            if i >= len(nums1):
                res.append(nums2[j])
                j += 1
            elif j >= len(nums2):
                res.append(nums1[i])
                i += 1
            elif nums1[i] < nums2[j]:
                res.append(nums1[i])
                i += 1
            else:
                res.append(nums2[j])
                j += 1

        return res

    nums = mergesort_helper(nums)
    return nums


def selection_sort(nums: list[int]) -> list[int]:
    for i, _ in enumerate(nums):
        for j in range(i + 1, len(nums)):
            if nums[i] > nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
    return nums


def insertion_sort(nums: list[int]) -> list[int]:
    for i, _ in enumerate(nums):
        j = i
        while j > 0 and nums[j] < nums[j - 1]:
            nums[j - 1], nums[j] = nums[j], nums[j - 1]
            j -= 1

    return nums


def timsort(nums: list[int]) -> list[int]:
    nums.sort()
    return nums


def is_sorted(nums) -> bool:
    if all(nums[i] <= nums[i + 1] for i in range(len(nums) - 1)):
        return True
    return False


if __name__ == "__main__":
    main()
