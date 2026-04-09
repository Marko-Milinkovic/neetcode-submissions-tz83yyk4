class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        result = []

        stack = [("(", 1, 0)]


        while stack:

            current_string, left_num, right_num = stack.pop()

            if len(current_string) == 2 * n:
                result.append(current_string)
            
            # rule for adding left parenthesis
            if left_num < n:
                stack.append((current_string + "(", left_num + 1, right_num))

            # rule for adding right parenthesis
            if right_num < left_num:
                stack.append((current_string + ")", left_num, right_num + 1))
        
        return result

                