class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        for c in s:
            if c in "({[" :
                stack.append(c)
                print(stack)

            elif c in ")}]":
                if not stack:
                    return False
                if c==")" and stack[-1]=="(":
                    stack.pop()
                elif c=="}" and stack[-1]=="{":
                    stack.pop()
                elif c=="]" and stack[-1]=="[":
                    stack.pop()
                else:
                    return False
                
        return not stack
            