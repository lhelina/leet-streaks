class Solution(object):
    def minimumIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        seen = {}
        for num in nums:
            if num in seen:
                seen[num] += 1
            else:
                seen[num] = 1

        maximum = 0  
        the_number = 0      

        for number, count in seen.items():
            if count > maximum:
                maximum = count
                the_number = number

        total = maximum  
        left_count = 0

        for i in range(len(nums) - 1):
            if nums[i] == the_number:
                left_count += 1

            right_count = total - left_count

            if left_count * 2 > (i + 1) and right_count * 2 > (len(nums) - i - 1):
                return i

        return -1