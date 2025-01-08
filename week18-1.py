# week18-1.py 二合一
class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        up, down = False, False
        for i in range(len(nums)-1):
            d= nums[i+1] - nums[i]
            if d>0: up = True
            if d<0: down = True

        if up and down: return False
        else: return True