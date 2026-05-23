class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        arr = []
        q = sorted(zip(position, speed))
        for i, j in q:
            arr.append((target - i)/j)
        #print(arr)
        stack = []
        result = len(position)
        for i in range(len(arr)):
            while stack and arr[stack[-1]] <= arr[i]:
                stack.pop()
                result -=1
            stack.append(i) 
        return result