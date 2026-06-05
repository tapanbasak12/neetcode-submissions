class TimeMap:
   #This problem is about returning the number less than or equal to the target in 
   #Binary seach
    def __init__(self):
        self.ob = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.ob:
            self.ob[key] = []
        self.ob[key].append([timestamp, value])
        #print(self.ob)
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.ob:
            return ""
        elif timestamp <  self.ob[key][0][0]:
            return ""
        l, r= 0, len(self.ob[key])-1
        while l<r:
            mid= l+(r-l)//2
            if self.ob[key][mid][0] == timestamp:
                return self.ob[key][mid][1]
            elif self.ob[key][mid][0] < timestamp:
                l=mid+1
            else:
                r=mid

        if self.ob[key][l][0] > timestamp:
            return self.ob[key][l - 1][1]
        return self.ob[key][l][1]