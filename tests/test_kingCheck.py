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
						translate('f','2') : Rook(0, translate('f','2'), []),
						translate('f','7') : King(0, translate('f','7'), []),
                        translate('f','5') : Queen(0, translate('f','5'), []),
						translate('g','7') : Pawn(0, translate('g','7'), []),
						translate('c','1') : King(1, translate('c','1'), []),
						translate('a','2') : Pawn(1, translate('a','2'), []),
						translate('b','3') : Pawn(1, translate('b','3'), []),
						}
        # self.chess_board.draw_Board()
        for to_update in self.chess_board.Fig_Pos:
            self.chess_board.Fig_Pos[to_update].update_poss_moves(self.chess_board)  # Initialize the chess board for each test case

    # Test to move pieces to empty squared
    def test_board2_moveKingToCheck(self):

        move_validity = check_if_move_is_possible(translate('c','1'), translate('b','1'),self.chess_board)
        check_validity = check_if_checkmate(1, translate('c','1'), translate('b','1'),self.chess_board)
        self.assertFalse(move_validity and check_validity and check_if_own_king_in_danger(translate('c','1'), translate('b','1'), self.chess_board))
        
        move_validity = check_if_move_is_possible(translate('c','1'), translate('c','2'),self.chess_board)
        check_validity = check_if_checkmate(1, translate('c','1'), translate('c','2'),self.chess_board)
        self.assertFalse(move_validity and check_validity and check_if_own_king_in_danger(translate('c','1'), translate('c','2'), self.chess_board))
    
    def test_board2_moveKingWithoutCheck(self):

        move_validity = check_if_move_is_possible(translate('c','1'), translate('d','1'),self.chess_board)
        check_validity = check_if_checkmate(1, translate('c','1'), translate('d','1'),self.chess_board)
        self.assertTrue(move_validity and check_validity and check_if_own_king_in_danger(translate('c','1'), translate('d','1'), self.chess_board))
    


if __name__ == '__main__':
    unittest.main()
