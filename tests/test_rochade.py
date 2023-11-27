import unittest
from chess import *

def translate(x,y):
    translate_a = {'a' : 0, 'b' : 1, 'c' : 2, 'd' : 3, 'e' : 4, 'f' : 5, 'g' : 6, 'h' : 7}
    translate_b = {'8' : 0, '7' : 1, '6' : 2, '5' : 3, '4' : 4, '3' : 5, '2' : 6, '1' : 7}

    # print("TYPE RETURNED IS ", type((translate_b[y], translate_a[x])))
    return (translate_b[y], translate_a[x])

class TestChessGame(unittest.TestCase):
    def setUp(self):
        print("SETUP")

        self.chess_board = Board()
        self.chess_board.Fig_Pos = {
						(0,0) : Rook(0, (0,0), []),
						(0,4) : King(0, (0,4), []),
						(0,7) : Rook(0, (0,7), []),	
						(1,0) : Pawn(0, (1,0), []),
						(1,1) : Pawn(0, (1,1), []),
						(1,2) : Pawn(0, (1,2), []),
						(1,3) : Pawn(0, (1,3), []),
						(1,4) : Pawn(0, (1,4), []),
						(1,5) : Pawn(0, (1,5), []),
						(1,6) : Pawn(0, (1,6), []),
						(1,7) : Pawn(0, (1,7), []),
						(7,0) : Rook(1, (7,0), []),
						(7,4) : King(1, (7,4), []),
						(7,7) : Rook(1, (7,7), []),	
						(6,0) : Pawn(1, (6,0), []),
						(6,1) : Pawn(1, (6,1), []),
						(6,2) : Pawn(1, (6,2), []),
						(6,3) : Pawn(1, (6,3), []),
						(6,4) : Pawn(1, (6,4), []),
						(6,5) : Pawn(1, (6,5), []),
						(6,6) : Pawn(1, (6,6), []),
						(6,7) : Pawn(1, (6,7), [])
						}
        # self.chess_board.draw_Board()
        for to_update in self.chess_board.Fig_Pos:
            self.chess_board.Fig_Pos[to_update].update_poss_moves(self.chess_board)  # Initialize the chess board for each test case

    # Test to move pieces to empty squared
    def test_rochade1(self):

        move = check_rochade(1, translate('e','1'), translate('h','1'), self.chess_board)
        self.assertTrue(move)

        move = check_rochade(0, translate('e','1'), translate('h','1'), self.chess_board)
        self.assertFalse(move)

    def test_rochade2(self):    
        move = check_rochade(1, translate('e','1'), translate('a','1'), self.chess_board)
        self.assertTrue(move)
        
    def test_rochade3(self):    
        move = check_rochade(0, translate('e','8'), translate('h','8'), self.chess_board)
        self.assertTrue(move)

    def test_rochade4(self):    
        move = check_rochade(0, translate('e','8'), translate('a','8'), self.chess_board)
        self.assertTrue(move)
    
    def test_rochade5(self):    
        move = check_rochade(1, translate('a','2'), translate('a','3'), self.chess_board)
        self.assertFalse(move)
        # self.chess_board.draw_Board()

if __name__ == '__main__':
    unittest.main()
