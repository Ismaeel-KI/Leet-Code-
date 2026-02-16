def reverseBits(n: int) -> int: 
    reverse = 0
    for i in range(32):
        reverse <<= 1
        reverse |= n & 1
        n >>= 1
    return reverse
    

