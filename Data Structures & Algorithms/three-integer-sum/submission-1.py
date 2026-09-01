class Solution:
    def twoSum(self, numbers: List[int], target: int) -> list[list[int]]:
        p = 0
        q = len(numbers) - 1
        pairs = []
        while p < q:
            total = numbers[p] + numbers[q]
            if total == target:
                pairs.append([numbers[p], numbers[q]])
                p += 1
                q -= 1
                while p < q and numbers[p] == numbers[p - 1]:  # skip duplicates
                    p += 1
                while p < q and numbers[q] == numbers[q + 1]:  # skip duplicates
                    q -= 1
            elif total < target:
                p += 1
            else:
                q -= 1
        return pairs

    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        result = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:  # skip duplicates
                continue
            target = -nums[i]
            pairs = self.twoSum(nums[i + 1:], target)
            for pair in pairs:
                result.append([nums[i]] + pair)
        return result