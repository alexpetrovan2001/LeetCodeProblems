from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        allArays = self.returnMultipleArrays(nums)
        if len(nums) == 1:
            result = nums[0]
        else:
            result = 0
        for i in allArays:
            noNegIndexes = i.pop()
            if noNegIndexes % 2 == 0:
                prod = self.calcProd(i)
                result = max(result, prod)
            else:
                negIndexes = []
                for j in range(len(i)):
                    if i[j] < 0:
                        negIndexes.append(j)
                if len(negIndexes) == 1 and len(i) > 1:
                    if len(i)-1 == negIndexes[0]:
                        prod = self.calcProd(i[:negIndexes[0]])
                    elif negIndexes[0]==0:
                        prod = self.calcProd(i[1:])
                    else:
                        prod = max(self.calcProd(i[:negIndexes[0]]), self.calcProd(i[negIndexes[0]+1:]))
                elif len(i)>1:
                    prod = max(self.calcProd(i[:negIndexes[-1]]), self.calcProd(i[negIndexes[0]+1:]))
                else:
                    prod = i[0]
                result = max(prod,result)
        return result


    def calcProd(self, nums: List[int]) -> int:
        res = 1
        for i in nums:
            res*=i
        return res

    def returnMultipleArrays(self, nums: List[int]) -> List[List[int]]:
        negIndexes = 0
        nonZeroArrays = []
        i = 0
        arrayToVerify = []
        while i < len(nums):
            if nums[i] == 0:
                if arrayToVerify:
                    arrayToVerify.append(negIndexes)
                    nonZeroArrays.append(arrayToVerify)
                    arrayToVerify=[]
                    negIndexes=0
            else:
                if nums[i]<0:
                    negIndexes+=1
                arrayToVerify.append(nums[i])
            i+=1
        if arrayToVerify:
            arrayToVerify.append(negIndexes)
            nonZeroArrays.append(arrayToVerify)
        return nonZeroArrays


sol = Solution()
sol.maxProduct([-2])