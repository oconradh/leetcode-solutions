class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        for i in range(0, int(len(s)/2)):
            storedValue = s[i]
            s[i] = s[len(s)-i-1]
            s[len(s)-i-1] = storedValue
