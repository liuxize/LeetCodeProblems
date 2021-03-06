class Solution(object):
    def moveZeroes(self, nums):
        j = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[j] =nums[i]
                j += 1
        
        while j < len(nums): #补充0 纠结好半天，一直想用[:]
        	nums[j] = 0
        	j += 1

    # 方法二
    def moveZeroes(self, nums):
        i, j = 0, 0
        while j < len(nums):
            if nums[j]==0:
                j += 1
            else:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j += 1
        return nums

                
                         
if __name__ == "__main__":
    nums = [0,1,0,3,12]
    s =Solution()
    s.moveZeroes(nums)
    print(nums)