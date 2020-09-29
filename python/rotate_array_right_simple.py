# We have to rotate the elements of the given array k times to the right.
from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        # speed up the rotation
        k %= len(nums)

        for i in range(k):
            previous = nums[-1]
            for j in range(len(nums)):
                nums[j], previous = previous, nums[j]


if __name__ == "__main__":
  solution = Solution()
  nums = [1, 2, 3, 4, 5, 6, 7]
  k = 3
  solution.rotate(nums, k)

  print(nums)