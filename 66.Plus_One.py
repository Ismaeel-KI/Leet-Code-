from typing import List


def plusOne(digits: List[int]) -> List[int]:
    tens = 1
    num = 0
    for i in digits[::-1]:
        num += i * tens
        tens *= 10
    num += 1
    digits.clear()
    for i in str(num):
        digits.append(int(i))
    print(digits)

plusOne([1,2,3])