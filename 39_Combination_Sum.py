#39. Combination Sum
from typing import List

def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

    result = []

    def backtrack(remaining, combo, start):

        # Base case: if remaining target is zero
        if remaining  == 0:

            # Found a valid combination
            result.append(combo[:])
            return
        
        # Explore further candidates
        for i in range(start, len(candidates)):

            # Skip candidates that exceed the remaining target
            if candidates[i] > remaining:
                continue

            # Include the candidate and continue exploring
            combo.append(candidates[i])

            # Recurse with updated remaining target
            backtrack(remaining - candidates[i], combo, i)

            # Backtrack: remove the last added candidate
            combo.pop()
    

    candidates.sort()
    backtrack(target, [], 0)
    return result

print(combinationSum(None, [2,3,6,7], 7))  # Output: [[7], [2,2,3]]
        