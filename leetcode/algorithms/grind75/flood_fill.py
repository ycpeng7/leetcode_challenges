class Solution:
    
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        color = image[sr][sc]
        if color == newColor:
            return image
        
        def dfs(i, j):
            if image[i][j] == newColor:
                return
            if image[i][j] == color:
                image[i][j] = newColor
                if i > 0:
                    dfs(i-1, j)
                if j > 0:
                    dfs(i, j - 1)
                if i < len(image) - 1:
                    dfs(i+1, j)
                if j < len(image[0]) - 1:
                    dfs(i, j+1)
        
        dfs(sr, sc)
        
        return image
        