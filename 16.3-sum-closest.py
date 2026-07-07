#
# @lc app=leetcode id=16 lang=python3
#
# [16] 3Sum Closest
#

# @lc code=start
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        result = nums[0] + nums[1] + nums[2]

        for i in range(len(nums) - 2):
            left, right = i + 1, len(nums) - 1

            while left < right:
                current_sum =  nums[i] + nums[left] + nums[right]
                if abs(current_sum - target) < abs(result - target):
                    result = current_sum

                if current_sum == target:
                    return target
                elif current_sum < target:
                    left += 1
                else:
                    right -= 1

        return result
                    
# @lc code=end

