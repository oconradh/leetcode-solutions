class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        tokenized = s.split()
        if len(tokenized) == 0:
            return 0
        else:
            return len(tokenized[-1])
