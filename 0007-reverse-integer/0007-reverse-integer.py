class Solution:
    def reverse(self, x: int) -> int:
        rev = 0
        while x != 0:
            if x >= 0:
                pop = x % 10
                x //= 10
            else:
                pop = -((-x) % 10)
                x = -((-x) // 10)
            if rev > 214748364 or (rev == 214748364 and pop > 7):
                return 0
            if rev < -214748364 or (rev == -214748364 and pop < -8):
                return 0
            rev = rev * 10 + pop
        return rev