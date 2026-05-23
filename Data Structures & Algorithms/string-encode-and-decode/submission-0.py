class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s 
        return res
            

    def decode(self, s: str) -> List[str]:
        res = []
        i=0
        while i < len(s):
            j=i #J iterates the integer , ex 10#abcdefghij
            while s[j] != '#':
                j+=1
            length_of_word = int (s[i:j])
            res.append(s[j+1: j+1+length_of_word])     
            i = j+1+length_of_word 
        return res
             
