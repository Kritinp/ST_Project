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

    def test_initial_board_setup_W_Rooks(self):
        initial_positions = self.chess_board.get_positions()
        self.assertTrue(translate('a','1') in initial_positions)
        self.assertTrue(translate('h','1') in initial_positions)

        self.assertEqual(initial_positions[translate('a','1')]._figure, 'Rook')
        self.assertEqual(initial_positions[translate('h','1')]._figure, 'Rook')
    
    def test_initial_board_setup_B_Rooks(self):
        initial_positions = self.chess_board.get_positions()
        self.assertTrue(translate('a','8') in initial_positions)
        self.assertTrue(translate('h','8') in initial_positions)

        self.assertEqual(initial_positions[translate('a','8')]._figure, 'Rook')
        self.assertEqual(initial_positions[translate('h','8')]._figure, 'Rook')

    def test_initial_board_setup_W_Knights(self):
        initial_positions = self.chess_board.get_positions()
        self.assertTrue(translate('b','1') in initial_positions)
        self.assertTrue(translate('g','1') in initial_positions)

        self.assertEqual(initial_positions[translate('b','1')]._figure, 'Knight')
        self.assertEqual(initial_positions[translate('g','1')]._figure, 'Knight')
    
    def test_initial_board_setup_B_Knights(self):
        initial_positions = self.chess_board.get_positions()
        self.assertTrue(translate('b','8') in initial_positions)
        self.assertTrue(translate('g','8') in initial_positions)

        self.assertEqual(initial_positions[translate('b','8')]._figure, 'Knight')
        self.assertEqual(initial_positions[translate('g','8')]._figure, 'Knight')
    
    def test_initial_board_setup_W_Bishops(self):
        initial_positions = self.chess_board.get_positions()
        self.assertTrue(translate('c','1') in initial_positions)
        self.assertTrue(translate('f','1') in initial_positions)

        self.assertEqual(initial_positions[translate('c','1')]._figure, 'Bishop')
        self.assertEqual(initial_positions[translate('f','1')]._figure, 'Bishop')
    
    def test_initial_board_setup_B_Bishops(self):
        initial_positions = self.chess_board.get_positions()
        self.assertTrue(translate('c','8') in initial_positions)
        self.assertTrue(translate('f','8') in initial_positions)

        self.assertEqual(initial_positions[translate('c','8')]._figure, 'Bishop')
        self.assertEqual(initial_positions[translate('f','8')]._figure, 'Bishop')
    
    def test_initial_board_setup_W_Queen(self):
        initial_positions = self.chess_board.get_positions()
        self.assertTrue(translate('d','1') in initial_positions)

        self.assertEqual(initial_positions[translate('d','1')]._figure, 'Queen')
    
    def test_initial_board_setup_B_Queen(self):
        initial_positions = self.chess_board.get_positions()
        self.assertTrue(translate('d','8') in initial_positions)

        self.assertEqual(initial_positions[translate('d','8')]._figure, 'Queen')

    def test_initial_board_setup_W_King(self):
        initial_positions = self.chess_board.get_positions()
        self.assertTrue(translate('e','1') in initial_positions)

        self.assertEqual(initial_positions[translate('e','1')]._figure, 'King')

    def test_initial_board_setup_B_King(self):
        initial_positions = self.chess_board.get_positions()
        self.assertTrue(translate('e','8') in initial_positions)

        self.assertEqual(initial_positions[translate('e','8')]._figure, 'King')
    
    def test_initial_board_setup_W_Pawns(self):
        initial_positions = self.chess_board.get_positions()
        self.assertTrue(translate('a','2') in initial_positions)
        self.assertTrue(translate('b','2') in initial_positions)
        self.assertTrue(translate('c','2') in initial_positions)
        self.assertTrue(translate('d','2') in initial_positions)
        self.assertTrue(translate('e','2') in initial_positions)
        self.assertTrue(translate('f','2') in initial_positions)
        self.assertTrue(translate('g','2') in initial_positions)
        self.assertTrue(translate('h','2') in initial_positions)

        self.assertEqual(initial_positions[translate('a','2')]._figure, 'Pawn')
        self.assertEqual(initial_positions[translate('b','2')]._figure, 'Pawn')
        self.assertEqual(initial_positions[translate('c','2')]._figure, 'Pawn')
        self.assertEqual(initial_positions[translate('d','2')]._figure, 'Pawn')
        self.assertEqual(initial_positions[translate('e','2')]._figure, 'Pawn')
        self.assertEqual(initial_positions[translate('f','2')]._figure, 'Pawn')
        self.assertEqual(initial_positions[translate('g','2')]._figure, 'Pawn')
        self.assertEqual(initial_positions[translate('h','2')]._figure, 'Pawn')
    
    def test_initial_board_setup_B_Pawns(self):
        initial_positions = self.chess_board.get_positions()
        self.assertTrue(translate('a','7') in initial_positions)
        self.assertTrue(translate('b','7') in initial_positions)
        self.assertTrue(translate('c','7') in initial_positions)
        self.assertTrue(translate('d','7') in initial_positions)
        self.assertTrue(translate('e','7') in initial_positions)
        self.assertTrue(translate('f','7') in initial_positions)
        self.assertTrue(translate('g','7') in initial_positions)
        self.assertTrue(translate('h','7') in initial_positions)

        self.assertEqual(initial_positions[translate('a','7')]._figure, 'Pawn')
        self.assertEqual(initial_positions[translate('b','7')]._figure, 'Pawn')
        self.assertEqual(initial_positions[translate('c','7')]._figure, 'Pawn')
        self.assertEqual(initial_positions[translate('d','7')]._figure, 'Pawn')
        self.assertEqual(initial_positions[translate('e','7')]._figure, 'Pawn')
        self.assertEqual(initial_positions[translate('f','7')]._figure, 'Pawn')
        self.assertEqual(initial_positions[translate('g','7')]._figure, 'Pawn')
        self.assertEqual(initial_positions[translate('h','7')]._figure, 'Pawn')


if __name__ == '__main__':
    unittest.main()
