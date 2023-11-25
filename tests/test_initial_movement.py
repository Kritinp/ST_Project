import unittest
from chess import *

def translate(x,y):
    translate_a = {'a' : 0, 'b' : 1, 'c' : 2, 'd' : 3, 'e' : 4, 'f' : 5, 'g' : 6, 'h' : 7}
    translate_b = {'8' : 0, '7' : 1, '6' : 2, '5' : 3, '4' : 4, '3' : 5, '2' : 6, '1' : 7}

    # print("TYPE RETURNED IS ", type((translate_b[y], translate_a[x])))
    return (translate_b[y], translate_a[x])

class TestChessGame(unittest.TestCase):
    def setUp(self):
        self.chess_board = Board()
        for to_update in self.chess_board.Fig_Pos:
            self.chess_board.Fig_Pos[to_update].update_poss_moves(self.chess_board)  # Initialize the chess board for each test case

    def test_initial_movement_W_Rooks(self):
        move_validity = check_if_move_is_possible(translate('a','1'), translate('a','4'),self.chess_board)
        self.assertFalse(move_validity)

        move_validity = check_if_move_is_possible(translate('h','1'), translate('h','4'),self.chess_board)
        self.assertFalse(move_validity)
    
    def test_initial_movement_B_Rooks(self):
        move_validity = check_if_move_is_possible(translate('a','8'), translate('a','4'),self.chess_board)
        self.assertFalse(move_validity)

        move_validity = check_if_move_is_possible(translate('h','8'), translate('h','4'),self.chess_board)
        self.assertFalse(move_validity)

    def test_initial_movement_W_Knights_impossible(self):
        move_validity = check_if_move_is_possible(translate('b','1'), translate('c','4'),self.chess_board)
        self.assertFalse(move_validity)

        move_validity = check_if_move_is_possible(translate('g','1'), translate('h','4'),self.chess_board)
        self.assertFalse(move_validity)
    
    def test_initial_movement_B_Knights_impossible(self):
        move_validity = check_if_move_is_possible(translate('b','8'), translate('a','5'),self.chess_board)
        self.assertFalse(move_validity)

        move_validity = check_if_move_is_possible(translate('g','8'), translate('g','5'),self.chess_board)
        self.assertFalse(move_validity)
    
    
    def test_initial_movement_W_Knights_possible(self):
        move_validity = check_if_move_is_possible(translate('b','1'), translate('c','3'),self.chess_board)
        self.assertTrue(move_validity)

        move_validity = check_if_move_is_possible(translate('g','1'), translate('h','3'),self.chess_board)
        self.assertTrue(move_validity)
    
    def test_initial_movement_B_Knights_possible(self):
        move_validity = check_if_move_is_possible(translate('b','8'), translate('a','6'),self.chess_board)
        self.assertTrue(move_validity)

        move_validity = check_if_move_is_possible(translate('g','8'), translate('h','6'),self.chess_board)
        self.assertTrue(move_validity)
    
    def test_initial_movement_W_Bishops(self):
        move_validity = check_if_move_is_possible(translate('c','1'), translate('b','2'),self.chess_board)
        self.assertFalse(move_validity)

        move_validity = check_if_move_is_possible(translate('f','1'), translate('e','2'),self.chess_board)
        self.assertFalse(move_validity)
    
    def test_initial_movement_B_Bishops(self):
        move_validity = check_if_move_is_possible(translate('c','8'), translate('d','7'),self.chess_board)
        self.assertFalse(move_validity)

        move_validity = check_if_move_is_possible(translate('f','8'), translate('g','7'),self.chess_board)
        self.assertFalse(move_validity)
    
    def test_initial_movement_W_Queen(self):
        move_validity = check_if_move_is_possible(translate('d','1'), translate('d','2'),self.chess_board)
        self.assertFalse(move_validity)
    
    def test_initial_movement_B_Queen(self):
        move_validity = check_if_move_is_possible(translate('d','8'), translate('d','7'),self.chess_board)
        self.assertFalse(move_validity)

    def test_initial_movement_W_King(self):
        move_validity = check_if_move_is_possible(translate('e','1'), translate('e','2'),self.chess_board)
        self.assertFalse(move_validity)

    def test_initial_movement_B_King(self):
        move_validity = check_if_move_is_possible(translate('e','8'), translate('e','7'),self.chess_board)
        self.assertFalse(move_validity)
    
    def test_initial_movement_W_Pawns_impossible(self):
        move_validity = check_if_move_is_possible(translate('a','2'), translate('b','3'),self.chess_board)
        self.assertFalse(move_validity)

        move_validity = check_if_move_is_possible(translate('d','2'), translate('e','3'),self.chess_board)
        self.assertFalse(move_validity)

        move_validity = check_if_move_is_possible(translate('h','2'), translate('g','3'),self.chess_board)
        self.assertFalse(move_validity)

    def test_initial_movement_W_Pawns_possible(self):
        move_validity = check_if_move_is_possible(translate('a','2'), translate('a','3'),self.chess_board)
        self.assertTrue(move_validity)

        move_validity = check_if_move_is_possible(translate('a','2'), translate('a','4'),self.chess_board)
        self.assertTrue(move_validity)

        move_validity = check_if_move_is_possible(translate('d','2'), translate('d','3'),self.chess_board)
        self.assertTrue(move_validity)

        move_validity = check_if_move_is_possible(translate('d','2'), translate('d','4'),self.chess_board)
        self.assertTrue(move_validity)

        move_validity = check_if_move_is_possible(translate('h','2'), translate('h','3'),self.chess_board)
        self.assertTrue(move_validity)

        move_validity = check_if_move_is_possible(translate('h','2'), translate('h','4'),self.chess_board)
        self.assertTrue(move_validity)
    
    def test_initial_movement_B_Pawns_impossible(self):
        move_validity = check_if_move_is_possible(translate('a','7'), translate('b','6'),self.chess_board)
        self.assertFalse(move_validity)

        move_validity = check_if_move_is_possible(translate('d','7'), translate('e','6'),self.chess_board)
        self.assertFalse(move_validity)

        move_validity = check_if_move_is_possible(translate('h','7'), translate('g','6'),self.chess_board)
        self.assertFalse(move_validity)

    def test_initial_movement_B_Pawns_possible(self):
        move_validity = check_if_move_is_possible(translate('a','7'), translate('a','6'),self.chess_board)
        self.assertTrue(move_validity)

        move_validity = check_if_move_is_possible(translate('a','7'), translate('a','5'),self.chess_board)
        self.assertTrue(move_validity)

        move_validity = check_if_move_is_possible(translate('d','7'), translate('d','6'),self.chess_board)
        self.assertTrue(move_validity)

        move_validity = check_if_move_is_possible(translate('d','7'), translate('d','5'),self.chess_board)
        self.assertTrue(move_validity)

        move_validity = check_if_move_is_possible(translate('h','7'), translate('h','6'),self.chess_board)
        self.assertTrue(move_validity)

        move_validity = check_if_move_is_possible(translate('h','7'), translate('h','5'),self.chess_board)
        self.assertTrue(move_validity)

if __name__ == '__main__':
    unittest.main()
