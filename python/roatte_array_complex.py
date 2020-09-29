from typing import List

# In this approach, we firstly reverse all the elements of the array. Then, reversing the first k elements followed by reversing the rest
# n−k elements gives us the required result.

# Original List                   : 1 2 3 4 5 6 7
# After reversing all numbers     : 7 6 5 4 3 2 1
# After reversing first k numbers : 5 6 7 4 3 2 1
# After revering last n-k numbers : 5 6 7 1 2 3 4


class Solution:
    def reverse(self, nums: list, start: int, end: int) -> None:
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start, end = start + 1, end - 1

    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k %= n

        self.reverse(nums, 0, n - 1)
        self.reverse(nums, 0, k - 1)
        self.reverse(nums, k, n - 1)


if __name__ == "__main__":
  solution = Solution()
  nums = [1, 2, 3, 4, 5, 6, 7]
  k = 3
  solution.rotate(nums, k)

  print(nums)