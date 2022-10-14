class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        """
        1. Traverse through the map and run backtracking.
        2. If node is not within boundary or not match the current char or is already visited, return False
        3. If neighbor is final character, success. Return True.
        4. If neighbor is next character, backtrack.
        5. If neighbor is not, skip it. If all neighbors failed, mark current as not visited and return False.
        6. The visited map can be replaced by modifying the current node on board to some character, and change it back if
        current solution doesn't work.
        """
        
        def backtrack(i, j, target_char_index, visited):
            in_boundary = i >= 0 and i < len(board) and j >= 0 and j < len(board[0])
            
            if not in_boundary:
                return False
            
            if board[i][j] != word[target_char_index] or visited[i][j]:
                return False

            if target_char_index == len(word) - 1:
                return True
            
            visited[i][j] = True
            
            neighbors = [[i + 1, j],
                         [i, j + 1],
                         [i - 1, j],
                         [i, j - 1]]
            
            for neighbor in neighbors:
                nei_i, nei_j = neighbor
                if backtrack(nei_i, nei_j, target_char_index + 1, visited):
                    return True
            visited[i][j] = False
            return False
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                visited = [[0 for _ in range(len(board[0]))] for _ in range(len(board))]
                if backtrack(i, j, 0, visited):
                    return True
            
        return False