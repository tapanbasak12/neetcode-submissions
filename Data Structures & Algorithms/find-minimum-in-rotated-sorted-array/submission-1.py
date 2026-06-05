class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums)<2:
            return nums[0]
        l, r = 0, len(nums)-1
        while l<r:
            mid= l+(r-l)//2
            if nums[r] < nums[mid]:
                l=mid+1 #solution does not stay on the left of mid
            else:
                r=mid
        return nums[l]