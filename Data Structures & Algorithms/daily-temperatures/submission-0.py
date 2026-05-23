class Solution:
    def dailyTemperatures(self, tem: List[int]) -> List[int]:
        stack=[]
        res=[0] * len(tem)
        for i in range (len(tem)):
            while stack and tem[stack[-1]] < tem[i]:
                index=stack.pop()
                res[index]= i-index
            stack.append(i)

        return res

        