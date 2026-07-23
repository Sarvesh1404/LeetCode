class Solution:
    def dayOfYear(self, date: str) -> int:
        y, m, d = map(int, date.split('-'))
        days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if (y % 400) == 0 or ((y % 4 == 0) and (y % 100!= 0)): days_in_month[2] = 29
        return d + sum(days_in_month[:m])