class Solution:
    def sumAndMultiply(self, n: int) -> int:
        x = ""
        s = 0

        for i in str(n):
            if i != "0":
                x += i
                s += int(i)

        if x == "":
            return 0

        return int(x) * s
