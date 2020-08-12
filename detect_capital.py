class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if word == word.upper():
            return True
        elif word == word.lower():
            return True
        elif word[1:] == (word.lower())[1:]:  
            return True
        else:
            return False
