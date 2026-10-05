class Solution:
    def isValid(self, s: str) -> bool:
        # ex. s = '[(])'
        # stack = [ '[' , '(' ] top
        # parentheses_map = { '}' : '{' , ']' : '[' , ')' : '(' }
        parentheses_map = { '}' : '{' , ']' : '[' , ')' : '(' }
        stack = []

        for p in s:
            if stack and p in parentheses_map:
                if stack[-1] == parentheses_map[p]: # p is closing parentheses
                    stack.pop()
                else:
                    return False
            else:
                stack.append(p)
        return True if not stack else False