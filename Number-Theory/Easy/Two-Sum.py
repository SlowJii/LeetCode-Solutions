
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}
        for i, num in enumerate(nums):
            res = target - num
            if res in hashMap:
                return [i, hashMap[res]]
            hashMap[num] = i