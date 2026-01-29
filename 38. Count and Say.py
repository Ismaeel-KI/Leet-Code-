"""
The count-and-say sequence is a sequence of digit strings defined by the recursive formula:
"""

def countAndSay(n: int) -> str:

    # Base Condition
    if n == 1:
        return "1"

    # Initialize
    result = '1'

    # Loop n - 1 times
    for _ in range(n-1):

        current = result
        result = ''
        i = 0

        # Iterate the word
        while  i < len(current):
            count = 1

            # Check if the following word is same as previous word
            while i + 1 < len(current) and current[i] == current[i + 1]:
                count += 1
                i += 1

            # Add the count with the word
            result += str(count) + current[i]
            i += 1

    return result

count = countAndSay(6)