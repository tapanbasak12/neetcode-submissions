class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r= 1, max(piles)
        def condition(k):
            total_hours=0
            for p in piles:
                if (p%k)!=0:
                    hours = (p // k) + 1
                else:
                    hours=p//k
                total_hours+=hours
            if total_hours <= h:
                return True
            else:
                return False
        
        while l<r:
            mid= l+(r-l)//2
            if condition(mid):
                r=mid
            else:
                l=mid+1
        return l 
