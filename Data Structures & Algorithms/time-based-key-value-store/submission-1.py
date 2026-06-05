class TimeMap:

    def __init__(self):
        self.ob = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.ob:
            self.ob[key] = []
        self.ob[key].append([timestamp, value])
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.ob:
            return ""
        elif timestamp <  self.ob[key][0][0]:
            return ""
        l, r= 0, len(self.ob[key])-1
        res = ""
        while l <= r:
            mid= l+(r-l)//2
            if self.ob[key][mid][0] == timestamp:
                return self.ob[key][mid][1]
            elif self.ob[key][mid][0] < timestamp:
                res = self.ob[key][mid][1]
                l=mid+1
            else:
                r=mid-1
        return res