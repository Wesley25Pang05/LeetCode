# Convert a non-negative integer num to its English words representation.

class Solution:

    convert = {
            1: " One", 2: " Two", 3: " Three",
            4: " Four", 5: " Five", 6: " Six",
            7: " Seven", 8: " Eight", 9: " Nine",
            10: " Ten", 11: " Eleven", 12: " Twelve",
            13: " Thirteen", 14: " Fourteen", 15: " Fifteen",
            16: " Sixteen", 17: " Seventeen", 18: " Eighteen",
            19: " Nineteen", 20: " Twenty", 30: " Thirty",
            40: " Forty", 50: " Fifty", 60: " Sixty",
            70: " Seventy", 80: " Eighty", 90: " Ninety"
        }

    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"
        commas = [" Billion", " Million", " Thousand", ""]
        number = ""
        num = str(num)
        while int(num) > 0:
            add = self.representThreeDigits(int(num) % 1000)
            if add:
                number = self.representThreeDigits(int(num) % 1000) + commas.pop() + number
            else:
                commas.pop()
            num = int(num) // 1000
        return number.lstrip()

    def representThreeDigits(self, num: int) -> str:
        number = ""
        if num > 99:
            number = self.convert[num // 100] + " Hundred"
            num %= 100
        if num in self.convert:
            return number + self.convert[num]
        elif num > 9:
            number += self.convert[num // 10 * 10]
            num %= 10
        if num > 0:
            number += self.convert[num]
        return number

# LeetCode Analysis:
# Key Idea: Divide the number into groups of three digits and map each group to English words.
# Current: Simulation / String
# Suggested: Simulation / String
# Current complexity: O(1)
# Suggested complexity: O(1)
# Readability: Excellent
# Structure: Excellent
