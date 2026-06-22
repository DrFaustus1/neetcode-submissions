class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(len(board)):
            horiz = set()
            for j in range(len(board[i])):
                if board[i][j] != "." and board[i][j] not in horiz:
                    horiz.add(board[i][j])
                elif board[i][j] in horiz:
                    return False

        for i in range(len(board)):
            vert = set()
            for j in range(len(board[i])):
                if board[j][i] != '.' and board[j][i] not in vert:
                    vert.add(board[j][i])
                elif board[j][i] in vert:
                    return False

        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                cubes = set()
                for r in range(3):
                    for k in range(3):
                        elem = board[i+r][j+k]
                        if elem != '.' and elem not in cubes:
                            cubes.add(elem)
                        elif elem in cubes:
                            return False 
        return True


                