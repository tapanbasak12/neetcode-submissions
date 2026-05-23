class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #Takes a list of strings returns a list of list of strings
        ans = defaultdict(list)
        for word in strs:
            count = [0] * 26
            for c in word:
                count[ord(c)-ord("a")]+=1 #This count list is the key
            ans[tuple(count)].append(word) #Only tuple can be used as a key in a dictionary
        #print(ans) (uncomment to understand)
        return ans.values()

#Time Complexity: m*n (m is the number of words, n is the averge length of each word)
