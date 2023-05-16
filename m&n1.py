
def print_chessboard(n,m):
    chessboard = [[None] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if(i+j) % 2 == 0:
                chessboard[i][j]= "◻︎"
            else:
                chessboard[i][j]= "◼︎"
    for row in chessboard:
        print("".join(row))