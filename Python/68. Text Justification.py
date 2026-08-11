# Given an array of strings words and a width maxWidth, format the text such that each line has exactly maxWidth characters and is fully (left and right) justified.
# You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly maxWidth characters.
# Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line does not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.
# For the last line of text, it should be left-justified, and no extra space is inserted between words.
# Note:
# A word is defined as a character sequence consisting of non-space characters only.
# Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.
# The input array words contains at least one word.

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        lines = []
        arr = []
        length = 0
        for i in words:
            if length + len(i) + len(arr) < maxWidth + 1:
                arr.append(i)
                length += len(i)
            else:
                if len(arr) > 1:
                    line = ""
                    addSpaces = maxWidth - length
                    for j in arr:
                        line += j + " " * math.ceil(addSpaces / (len(arr) - 1))
                        addSpaces -= 1
                    lines.append(line.strip())
                else:
                    lines.append(arr[0] + " " * (maxWidth - length))
                arr = [i]
                length = len(i)
        line = ""
        for k in arr:
            line += k + " "
        lines.append((line + " " * (maxWidth - length - len(arr)))[:maxWidth])
        return lines

# LeetCode Analysis:
# Key Idea: Greedy line packing with precise space distribution logic.
# Current: Array / String / Simulation
# Suggested: Array / String / Simulation
# Current complexity: O(N)
# Suggested complexity: O(N)
# Readability: Excellent
# Structure: Excellent
