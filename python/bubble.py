from random import randint

class Solution:
    def acs(self, nums: list[int]) -> list[int]:
        for i in range(len(nums) - 1):
            swapped = False
            for j in range(len(nums) - 1 - i):
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
                swapped = True
                if not swapped:
                    break
        return nums
    
test = Solution()
l = list()
for _ in range(5000):
    l.append(randint(1, 10))

print(l)
x = test.acs(l)
print(x)