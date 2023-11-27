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
						(0,1) : Knight(0, (0,1), []),
						(0,6) : King(0, (0,6), []),
						(2,5) : Bishop(0, (2,5), []),
                        (1,2) : Queen(0, (1,2), []),
						(0,3) : Rook(0, (0,3), []),	
						(2,0) : Pawn(0, (2,0), []),
						(1,1) : Pawn(0, (1,1), []),
						(2,3) : Pawn(0, (2,3), []),
						(1,5) : Pawn(0, (1,5), []),
						(1,6) : Pawn(0, (1,6), []),
						(1,7) : Pawn(0, (1,7), []),
						(7,2) : Rook(1, (7,2), []),
						(2,7) : Bishop(1, (2,7), []),
						(4,4) : Queen(1, (4,4), []),
						(7,6) : King(1, (7,6), []),
						(5,3) : Bishop(1, (5,3), []),
						(7,4) : Rook(1, (7,4), []),	
						(4,0) : Pawn(1, (4,0), []),
						(5,2) : Pawn(1, (5,2), []),
						(3,3) : Pawn(1, (3,3), []),
						(6,5) : Pawn(1, (6,5), []),
						(6,6) : Pawn(1, (6,6), []),
						(6,7) : Pawn(1, (6,7), [])
						}
        # self.chess_board.draw_Board()
        for to_update in self.chess_board.Fig_Pos:
            self.chess_board.Fig_Pos[to_update].update_poss_moves(self.chess_board)  # Initialize the chess board for each test case

    # Test to move pieces to empty squared
    def test_board1_moveToUnoccupiedSquare1(self):

        move_validity = check_if_move_is_possible(translate('a','4'), translate('a','5'),self.chess_board)
        self.assertTrue(move_validity and check_if_own_king_in_danger(translate('a','4'), translate('a','5'), self.chess_board))

        move_validity = check_if_move_is_possible(translate('e','4'), translate('f','5'),self.chess_board)
        self.assertTrue(move_validity and check_if_own_king_in_danger(translate('e','4'), translate('f','5'), self.chess_board))

        move_validity = check_if_move_is_possible(translate('g','1'), translate('h','1'),self.chess_board)
        self.assertTrue(move_validity and check_if_own_king_in_danger(translate('g','1'), translate('h','1'), self.chess_board))

        move_validity = check_if_move_is_possible(translate('d','3'), translate('b','1'),self.chess_board)
        self.assertTrue(move_validity and check_if_own_king_in_danger(translate('d','3'), translate('b','1'), self.chess_board))

    # Test to move pieces to empty square through friendly pieces
    def test_board1_moveToUnoccupiedSquare2(self):

        # self.chess_board.draw_Board()
        move_validity = check_if_move_is_possible(translate('e','1'), translate('b','1'),self.chess_board)
        self.assertFalse(move_validity and check_if_own_king_in_danger(translate('e','1'), translate('b','1'), self.chess_board))

        move_validity = check_if_move_is_possible(translate('d','3'), translate('f','5'),self.chess_board)
        self.assertFalse(move_validity and check_if_own_king_in_danger(translate('d','3'), translate('f','5'), self.chess_board))

        move_validity = check_if_move_is_possible(translate('e','4'), translate('c','6'),self.chess_board)
        self.assertFalse(move_validity and check_if_own_king_in_danger(translate('e','4'), translate('c','6'), self.chess_board))
    
    # Test to move pieces to capture enemy pieces or land on friendly pieces
    def test_board1_moveToCapture(self):
        move_validity = check_if_move_is_possible(translate('d','3'), translate('a','6'),self.chess_board)
        self.assertTrue(move_validity and check_if_own_king_in_danger(translate('d','3'), translate('a','6'), self.chess_board))
        currPositions = self.chess_board.get_positions()
        self.assertEqual(currPositions[translate('a','6')]._figure, 'Bishop')

        move_validity = check_if_move_is_possible(translate('e','4'), translate('d','5'),self.chess_board)
        self.assertFalse(move_validity and check_if_own_king_in_danger(translate('e','4'), translate('d','5'), self.chess_board))  
        currPositions = self.chess_board.get_positions()
        self.assertEqual(currPositions[translate('e','4')]._figure, 'Queen')

        move_validity = check_if_move_is_possible(translate('h','6'), translate('g','7'),self.chess_board)
        self.assertTrue(move_validity and check_if_own_king_in_danger(translate('h','6'), translate('g','7'), self.chess_board))
        currPositions = self.chess_board.get_positions()
        self.assertEqual(currPositions[translate('g','7')]._figure, 'Bishop')

if __name__ == '__main__':
    unittest.main()
