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

