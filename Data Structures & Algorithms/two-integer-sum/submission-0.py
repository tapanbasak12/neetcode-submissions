class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index_dict={}
        for index,element in enumerate(nums):
            if target-element in index_dict:
                return [index_dict[target-element], index]
            index_dict[element] = index 
                
