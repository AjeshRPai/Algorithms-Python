class Solution:
    def reverseBits(self, n: int) -> int:
        # ways to do
        # 1. shift the bits?
        res = 0
        for i in range(32):
            # shifts by i digits so first digit by 1,
            # 2nd digit by 2 and then so on
            # and then makes an and operation
            # so what happens is the first digit will be and
            # and then it will be
            bit = (n >> i) & 1
            res += (bit << (31 - i))
        return res