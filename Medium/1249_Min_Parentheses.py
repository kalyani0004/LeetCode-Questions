#Problem Number:1249
#Difficulty:Medium
#Time Complexity:O(n)
#Space Complexity:O(n)

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        s=list(s)
        stack=[]

        for i,char in enumerate(s):
            if char=="(":
                stack.append(i)
            elif char==")":
                if stack:
                    stack.pop()
                else:
                    s[i]=""
        
        while stack:
            s[stack.pop()]=""
        return ''.join(s)
