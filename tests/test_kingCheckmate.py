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
						(0,0) : King(0, (0,0), []),
						(5,1) : Rook(1, (5,1), []),
						(6,1) : Queen(1, (6,1), []),
						(7,4) : King(1, (7,4), [])
						}
        # self.chess_board.draw_Board()
        for to_update in self.chess_board.Fig_Pos:
            self.chess_board.Fig_Pos[to_update].update_poss_moves(self.chess_board)  # Initialize the chess board for each test case

    
    def test_kingCheck(self):

            # self.chess_board.draw_Board()
	
            move_validity = check_if_move_is_possible(translate('b','2'), translate('a','2'),self.chess_board)

            move = check_if_own_king_in_danger(translate('b','2'), translate('a','2'), self.chess_board)
            for to_update in self.chess_board.Fig_Pos:
                   self.chess_board.Fig_Pos[to_update].update_poss_moves(self.chess_board)

            check_mate = check_if_checkmate(1, translate('b','2'), translate('a','2'),self.chess_board)
            # self.assertTrue(move_validity and not check_mate and check_if_own_king_in_danger(translate('d','4'), translate('f','2'), self.chess_board))
            self.assertTrue(check_mate and move_validity and move)
            # self.chess_board.draw_Board()


if __name__ == '__main__':
    unittest.main()















