
class Solution(object):

    def twoSum(self, nums, target):
    
       for i in range(len(nums)):
           print(nums[i])
           for j in range(i + 1, len(nums)):
               if nums[i] + nums[j] == target:
                   return [i, j]





sol = Solution()

nums = [1, 2, 3, 4, 5, 6]

target = 10


result = sol.twoSum(nums, target)

print(result)
