class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_dict = {}
        for item in nums:
            if item in count_dict:
                count_dict[item] = count_dict[item] + 1
            else: 
                count_dict[item] =1
        #print(count_dict)        
        sorted_dict_by_count = dict(sorted(count_dict.items(), key=lambda item: item[1], reverse=True))
        first_k_keys = list(sorted_dict_by_count.keys())[:k]
        return first_k_keys

