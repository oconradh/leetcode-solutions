class Solution:
    def reverseWords(self, s: str) -> str:
        split_string = s.split()
        if len(split_string) != 0:
            reversed_string = split_string[0][::-1]
            for i in range(1,len(split_string)):
                reversed_string = reversed_string + " " + split_string[i][::-1]
            return reversed_string
        else:
            return ""
