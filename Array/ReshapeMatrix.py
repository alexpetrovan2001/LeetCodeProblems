import queue
from typing import List


class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        result = []
        m = len(mat)
        if m<=0:
            return mat
        n = len(mat[0])
        if n <= 0:
            return mat
        if min(r,c) > max(m, n):
            return mat
        if r*c != m*n:
            return mat
        elems = []
        for i in range(m):
            for j in range(n):
                elems.append(mat[i][j])
        for i in range(r):
            row = []
            for j in range(c):
                row.append(elems.pop(0))
            result.append(row)
        return result

    def matrixReshape2(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        # Not working for the moment
        if len(mat)>0 and r*c != len(mat)*len(mat[0]):
            return mat
        result = []
        for i in mat:
            row = []
            count = 0
            while count < c and i:
                row.append(i.pop(0))
                count+=1
            result.append(row)
        return result


sol = Solution()
sol.matrixReshape2([[1,2],[3,4]],1,4)


