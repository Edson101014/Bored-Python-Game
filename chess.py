class ChessPiece:
    def __init__(self, color):
        self.color = color

    def __str__(self):
        return self.symbol

class King(ChessPiece):
    symbol = 'K'

class Queen(ChessPiece):
    symbol = 'Q'

class Rook(ChessPiece):
    symbol = 'R'

class Bishop(ChessPiece):
    symbol = 'B'

class Knight(ChessPiece):
    symbol = 'N'

class Pawn(ChessPiece):
    symbol = 'P'

class ChessBoard:
    def __init__(self):
        self.board = [[' ' for _ in range(8)] for _ in range(8)]
        self.setup_board()

    def setup_board(self):
        for i in range(8):
            self.board[1][i] = Pawn('black')
            self.board[6][i] = Pawn('white')

        placement = [Rook, Knight, Bishop, Queen, King, Bishop, Knight, Rook]
        for i, piece in enumerate(placement):
            self.board[0][i] = piece('black')
            self.board[7][i] = piece('white')

    def display(self):
        for row in self.board:
            print(' '.join(str(piece) if piece != ' ' else '.' for piece in row))

if __name__ == "__main__":
    chess_board = ChessBoard()
    chess_board.display()