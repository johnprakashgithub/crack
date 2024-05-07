class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = []
        for index, num in enumerate(nums):
            if num <= target:
                result.append(index)
                next_num = target - num
                for next_index, item in enumerate(nums[index+1:]):
                    if item == next_num:
                        result.append(index+1+next_index)
                        return result
            result = []
