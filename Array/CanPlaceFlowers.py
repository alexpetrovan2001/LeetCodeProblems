from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if len(flowerbed) == 1:
            return True if flowerbed[0] == 0 else False
        i = 2
        if flowerbed[0] == 0 and flowerbed[1] == 0:
            n-=1
        elif flowerbed[1] == 1:
            i = 3
        while i<len(flowerbed)-1:
            if flowerbed[i] == 1:
                i+=2
            if i==len(flowerbed)-1:
                break
            if flowerbed[i] == 0 :
                if flowerbed[i-1] == 0 and flowerbed[i+1] == 0:
                    n-=1
                    i+=2
                else:
                    i+=1
        if i == len(flowerbed)-1:
            if flowerbed[i] == 0 and flowerbed[i-1] == 0:
                n-=1
        return True if n<=0 else False

sol = Solution()
sol.canPlaceFlowers([1,0,0,0,1,0,0], 2)