"""
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the
largest sum and return its sum.

In the DP solution, we need to create an intermediate storage
    sums[0] = nums[0]
    sums[i] = max(sums[i-1] + nums[i], nums[i]

The end result is max(sums[i]). Note that this is not necessarily sums[-1].

e.g. for nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
max_sums[0] = -2 (only one option)
max_sums[1] = max(-2 + 1, 1) = 1
max_sums[2] = max(1, -3) = 1
max_sums[3] = max(1, 4) = 4
and so on.
"""


def max_cont_subset(nums):
    # Empty array: return o
    if not nums:
        return 0
    # Only one element: return that element
    if len(nums) == 1:
        return nums[0]

    # intermediate results in a 2D array
    # max_sums[i][j]: maximum subset sum for the subsequence nums[i]....nums[j]
    sums = [0] * len(nums)

    # initialization
    for i, e in enumerate(nums):
        if i == 0:
            sums[i] = e
            continue
        sums[i] = max(sums[i-1] + e, e)

    # Final result is the last element of max_sums
    return max(sums)


if __name__ == '__main__':
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    result = max_cont_subset(nums)
    print(result)
    assert result == 6
