class Solution:
    def floodFill(self, image, sr, sc, color):

        old = image[sr][sc]

        if old == color:
            return image

        rows = len(image)
        cols = len(image[0])

        def dfs(r, c):

            if (r < 0 or r >= rows or
                c < 0 or c >= cols or
                image[r][c] != old):
                return

            image[r][c] = color

            dfs(r + 1, c)  # Down
            dfs(r - 1, c)  # Up
            dfs(r, c + 1)  # Right
            dfs(r, c - 1)  # Left

        dfs(sr, sc)

        return image