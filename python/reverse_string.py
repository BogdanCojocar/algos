# Write a function that reverses a string. The input string is given as an array of characters char[].
# Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        start = 0
        end = len(s) - 1

        while start < end:
            s[start], s[end] = s[end], s[start]
            start += 1
            end -= 1


if __name__ == "__main__":
  solution = Solution()
  s = ['a', 'b', 'c', 'd']
  solution.reverseString(s)

  print(s)