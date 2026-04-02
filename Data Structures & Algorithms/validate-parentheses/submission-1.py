class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        for i in range(len(s)):  # Fixed: added parentheses
            # Opening brackets - push to stack
            if s[i] == '(' or s[i] == '[' or s[i] == '{':  # Fixed: use s[i], not str[i] or s
                stack.append(s[i])  # Fixed: use append(), push current character
            
            # Closing brackets - check if they match
            elif s[i] == ')' or s[i] == ']' or s[i] == '}':
                # Check if stack is empty first
                if not stack:
                    return False
                
                # Check if brackets match
                if (s[i] == ')' and stack[-1] == '(') or \
                   (s[i] == ']' and stack[-1] == '[') or \
                   (s[i] == '}' and stack[-1] == '{'):
                    stack.pop()
                else:
                    return False
        
        # Stack should be empty if all brackets are matched
        return len(stack) == 0