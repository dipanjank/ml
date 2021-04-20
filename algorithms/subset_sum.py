"""
Given a set of non-negative integers, and a value sum, determine if there is a subset of the given set with sum equal to given sum.

Example:

Input: set[] = {3, 34, 4, 12, 5, 2}, sum = 9
Output: True
There is a subset (4, 5) with sum 9.

Input: set[] = {3, 34, 4, 12, 5, 2}, sum = 30
Output: False
There is no subset that add up to 30.
"""


def subset_sum_recursive(nums, target):
    # Base case of the recursive function
    if not nums:
        return False
    if len(nums) == 1:
        return nums[0] == target

    # Otherwise, take the first n-1 elements from nums
    # return True if
    # 1. these sum to target, or
    # 2. target - last element
    subset = nums[:-1]
    return subset_sum_recursive(subset, target) or subset_sum_recursive(subset, target - nums[-1])


def subset_sum_dynamic(nums, target):
    if not nums:
        return False
    if len(nums) == 1:
        return nums[0] == target

    # temporary table to store results
    # First dimension is number of elements in nums + 1
    # Second dimension is target + 1
    # subset_sums[i][j] = True if the subset 0, 1, 2, ..., i-1 contains a target j, False otherwise
    # Set subset_sums[i][0] = True. This is to handle the base case.
    # The recurrence step is:
    # subset_sums[i][j] = subset_sums[i-1][j] or subset_sums[i-1][j-nums[i-1]]
    # where subset_sums[i-1][j] indicates if elements 0, 1, ... i-1 in nums contain target j
    # subset_sums[i-1][j-nums[i-1]] indicates if elements 0, 1, ..., i-1 in nums contain target j-nums[i-1]
    n = len(nums)
    subset_sums = [[False] * (target+1) for _ in range(n+1)]

    for i in range(n+1):
        subset_sums[i][0] = True

    for i in range(1, n+1):
        for j in range(1, target+1):
            if j >= nums[i-1]:
                subset_sums[i][j] = subset_sums[i-1][j] or subset_sums[i-1][j-nums[i-1]]
            else:
                subset_sums[i][j] = subset_sums[i-1][j]

    return subset_sums[n][-1]


if __name__ == '__main__':
    nums = [3, 34, 4, 12, 5, 2]
    result = subset_sum_dynamic(nums, 14)
    assert result

    result = subset_sum_recursive(nums, 60)
    assert result

    result = subset_sum_recursive(nums, 30)
    assert not result
