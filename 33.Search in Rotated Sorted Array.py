class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = len(nums) - 1
        while left <= right :
            mid = ( left + right ) // 2
            if nums[mid] == target :
                return mid
            elif nums[mid]>target and (target>nums[left] or nums[left]>nums[mid]) or target>nums[left] and nums[left]>nums[mid] :
                right = mid - 1
            else:
                left = mid + 1
        return -1