from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        numsFreq = dict()
        result = []
        for i in nums:
            if i in numsFreq:
                numsFreq[i]+=1
            else:
                numsFreq[i]=1
        nums = list(numsFreq.keys())
        if 0 in numsFreq and numsFreq[0]>=3:
            result.append([0,0,0])
        for i in range(len(nums)-1):
            if numsFreq[nums[i]] >= 2:
                if nums[i] != 0 and (nums[i]*-2) in numsFreq:
                    result.append([nums[i],nums[i],-2*nums[i]])
            for j in range(i+1, len(nums)):
                if nums[i] !=0 and nums[j] != 0 and -(nums[i]+nums[j]) in numsFreq:
                    if nums[i]+nums[j]-(nums[i]+nums[j]) == 0:
                        result.append([nums[i], nums[j], nums[i]+nums[j]])
        return result

    def threeSum2(self, nums: List[int]) -> List[List[int]]:
        # optimized way

        res = []

        nums.sort()

        for i in range(len(nums)):

            if i > 0 and nums[i] == nums[i - 1]:
                continue

            l = i + 1
            r = len(nums) - 1

            while (l < r):
                if nums[i] + nums[l] + nums[r] == 0:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1

                elif nums[i] + nums[l] + nums[r] > 0:
                    r -= 1

                else:
                    l += 1
        return res

sol = Solution()
sol.threeSum([3,0,-2,-1,1,2])