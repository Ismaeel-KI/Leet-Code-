class Solution:
    def addBinary(self, a: str, b: str) -> str:
        int_a = int(a, 2)
        int_b = int(b, 2)
        int_c = int_a + int_b

        c = bin(int_c)[2:]

        return c