class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_dict = {}
        for item in nums:
            if item in count_dict: #o(1) search in hash table takes o(1)
                count_dict[item] = count_dict[item] + 1 
            else:
                count_dict[item] = 1
        
        freq=[] #The frequency is the index and each index contains a list (basically a list of lists)
        for i in range (len(nums)+1):   
            freq.append([])
        for num, count in count_dict.items():                  
            freq[count].append(num)         
        print(freq)
        res=[]
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res
