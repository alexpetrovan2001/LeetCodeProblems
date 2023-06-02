from typing import List


def plusOne(digits: List[int]) -> List[int]:
    index = len(digits) - 1
    while index >= 0:
        if digits[index] == 9:
            if index == 0 and digits[index] == 9:
                digits[index] = 0
                digits.insert(0, 1)
                return digits
            digits[index] = 0
            index -= 1
        else:
            digits[index] += 1
            return digits

print(plusOne([9,9]))