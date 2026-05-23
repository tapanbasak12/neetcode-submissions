class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        prefix=[0]*n 
        prefix[0]=nums[0]
        print(prefix[0])
        for i in range(1,n):
            prefix[i]= nums[i]*prefix[i-1]
        print(prefix)
        suffix = [0]*n
        suffix[n-1]=nums[n-1]
        for i in range(n-2, -1, -1):
            suffix[i]=suffix[i+1]*nums[i]
        print(suffix)
        res = [0]*n
        for i in range(n):
            if(i==0): 
                res[i]= 1 * suffix[i+1]
            elif (i==n-1):
                res[i] = prefix[i-1]* 1
            else:
                res[i]=prefix[i-1]*suffix[i+1]
        print(res)
        return res   


