class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for i in tokens:
            if i.isdigit() or (len(i) > 1 and i[0] == '-'):
                stack.append(int(i))
            else:
                b= stack.pop()
                a= stack.pop()
                if i=='+':
                    ans=a+b
                    stack.append(ans)
                elif i=='-':
                    ans=a-b
                    stack.append(ans)
                elif i=='*':
                    ans=a*b
                    stack.append(ans)
                elif i=='/':
                    ans= int(a/b)
                    stack.append(ans)
            
        return stack[-1]

                 
                
        