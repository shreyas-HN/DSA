class Solution:
    def isValid(self, s: str) -> bool:
        bracket_map = {")": "(", "}": "{", "]": "["}
        stack=[]
        for char in s:
        # If the character is a closing bracket
            if char in bracket_map:
                # Pop the top element if stack isn't empty, else assign a dummy value
                top_element = stack.pop() if stack else '#'
                
                # If the opening bracket doesn't match the map's value, it's invalid
                if bracket_map[char] != top_element:
                    return False
            else:
                # It's an opening bracket, push it onto the stack
                stack.append(char)
            
    # If the stack is empty, all brackets were matched correctly
        return not stack
        