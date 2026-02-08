from typing import List

def firstMissingPositive(nums: List[int]) -> int:

    n = len(nums)

    for i in range(n):
        while 1 <= nums[i] <= n and nums[i] != nums[nums[i] - 1]:
            correct = nums[i] - 1
            nums[i], nums[correct] = nums[correct], nums[i]
    
    for i in range(n):
        if nums[i] != i + 1:
            missing = i + 1
            return missing

    return n + 1

print(firstMissingPositive(nums = [7,8,9,11,1]))