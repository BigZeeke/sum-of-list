def sum_of_lists(nums: list[int]) -> int:
    if len(nums) == 0:
        return 0
    else:
        return nums[0] + sum_of_lists(nums[1:])
