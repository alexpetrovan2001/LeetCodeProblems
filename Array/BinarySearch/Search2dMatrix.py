from typing import List


class Solution:
    # Initial solution beats only 53 % time and 26 % memory
    def searchMatrix2(self, matrix: List[List[int]], target: int) -> bool:
        notFound = True
        rowToSearch = []
        while matrix and notFound:
            mid = len(matrix) // 2
            if matrix[mid][0] <= target <= matrix[mid][-1]:
                notFound = False
                rowToSearch = matrix[mid]
            elif matrix[mid][0] > target:
                matrix = matrix[:mid]
            else:
                matrix = matrix[mid + 1:]
        if notFound:
            return False
        else:
            while rowToSearch:
                mid = len(rowToSearch) // 2
                if rowToSearch[mid] == target:
                    return True
                elif rowToSearch[mid] > target:
                    rowToSearch = rowToSearch[:mid]
                else:
                    rowToSearch = rowToSearch[mid + 1:]
            return False

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Beats 98 % time and  94 % memory
        while matrix:
            mid = len(matrix) // 2
            if matrix[mid][0] <= target <= matrix[mid][-1]:
                while matrix[mid]:
                    mid2 = len(matrix[mid]) // 2
                    if matrix[mid][mid2] == target:
                        return True
                    elif matrix[mid][mid2] > target:
                        matrix[mid] = matrix[mid][:mid2]
                    else:
                        matrix[mid] = matrix[mid][mid2 + 1:]
                return False
            elif matrix[mid][0] > target:
                matrix = matrix[:mid]
            else:
                matrix = matrix[mid + 1:]
        return False


sol = Solution()
print(sol.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,50]], 3))
