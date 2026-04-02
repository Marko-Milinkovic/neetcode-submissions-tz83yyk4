class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        if digits == "":
            return []

        res = ['']
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }

        for digit in digits:
            letters = digitToChar[digit]
            new_res = []
            for comb in res:
                for letter in letters:
                    new_res.append(comb + letter)
            
            res = new_res

        return res







