class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        twosumdict = dict()
        for i,j in enumerate(nums):
            if(target-j) in twosumdict:
                return [twosumdict[target-j], i]
                #insert(3,0)
            else:
                twosumdict[j]=i 

                
        
       