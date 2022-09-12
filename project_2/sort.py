'''
Project 2: sort

'''

import math
import random
import time


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



def main():
    random.seed(1111)
    max_num = 100000000
    array_len = 10000000

    nums = random.sample(range(max_num), k=array_len)
    # nums: list = [1,2,3,4,5]

    print_results(nums)



def quicksort(nums):
    nums.sort()
    nums

def mergesort(nums):
    nums.sort()
    nums

def selection_sort(nums):
    nums.sort()
    nums

def insertion_sort(nums):
    nums.sort()
    nums

def timsort(nums):
    nums.sort()
    nums

def is_sorted(nums):
    if not isinstance(nums, list):
        return False
    max_val = 0
    for num in nums:
        if num > max_val:
            return False
        if not isinstance(num, int):
            return False
    return True




if __name__ == "__main__":
    main()
