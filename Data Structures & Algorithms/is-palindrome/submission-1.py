class Solution:
    def isPalindrome(self, s: str) -> bool:
        p=0
        q=len(s)-1

        while(p<q):
            if(s[p].isalnum() and s[q].isalnum()):
                if(s[p].lower()==s[q].lower()):
                    #print(s[p], s[q])
                    p=p+1
                    q=q-1
                else:
                    return False
            elif not s[p].isalnum():
                p=p+1
            else:
                q=q-1

        return True