class Solution:
    def dailyTemperatures(self, temperatures):
        l = [0] * len(temperatures)
        stack = []

        for i in range(len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                index = stack.pop()
                l[index] = i - index

            stack.append(i)

        return l    