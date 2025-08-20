"""
Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

Example 1:

Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
Example 2:

Input: numRows = 1
Output: [[1]]
"""

from typing import List

from pydantic.v1.utils import generate_model_signature


def generate(numRows: int) -> List[List[int]]:

    pascaltriangle = [[1]]

    def next_row(last_row: list[int]):
        new_row = [1]
        for i in range(len(last_row)-1):
                new_value = last_row[i] + last_row[i+1]
                new_row.append(new_value)
        new_row.append(1)
        return new_row

    for _ in range(numRows-1):
        last_row = pascaltriangle[-1]
        pascaltriangle.append(next_row(last_row))

    return pascaltriangle

print(generate(5))

