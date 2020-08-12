class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        stringInt = ""
        for element in digits:
            stringInt += str(element)
        stringInt = str(int(stringInt) + 1)
        intList = []
        for i in range(0,len(stringInt)):
            intList.append(stringInt[i])
        return intList
