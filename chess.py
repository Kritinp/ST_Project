class Board(object):
	def __init__(self):
		self.Fig_Pos = {
						(0,0) : Rook(0, (0,0), []),
						(0,1) : Knight(0, (0,1), []),
						(0,2) : Bishop(0, (0,2), []),
						(0,3) : Queen(0, (0,3), []),
						(0,4) : King(0, (0,4), []),
						(0,5) : Bishop(0, (0,5), []),
						(0,6) : Knight(0, (0,6), []),
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
						(7,1) : Knight(1, (7,1), []),
						(7,2) : Bishop(1, (7,2), []),
						(7,3) : Queen(1, (7,3), []),
						(7,4) : King(1, (7,4), []),
						(7,5) : Bishop(1, (7,5), []),
						(7,6) : Knight(1, (7,6), []),
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

	def get_positions(self):
		return self.Fig_Pos

	def update_positions(self, old_position, new_position):
		self.Fig_Pos[new_position] = self.Fig_Pos[old_position]
		del self.Fig_Pos[old_position]

	def update_position_rochade(self, old_position, new_position):
		p1 = self.Fig_Pos[old_position]
		p2 = self.Fig_Pos[new_position]

		self.Fig_Pos[old_position] = p2
		self.Fig_Pos[new_position] = p1



class Figure(object):
	def __init__(self, color, position, poss_moves):
		self._color = color
		self.position = position
		self.poss_moves = poss_moves

	def get_poss_moves(self):
		return self.poss_moves

	def get_position(self):
		return self.position

	def get_color(self):
		return self._color


class King(Figure):	
	def __init__(self, color, position, poss_moves, figure = 'King'):
		Figure.__init__(self, color, position, poss_moves)
		self._figure = figure
		self.already_moved = False

	def get_sourrounding(self):
		i,j = self.position[0], self.position[1]
		sur = [(i-1, j-1), (i-1, j), (i-1, j+1), (i, j-1), (i, j+1), (i+1, j-1), (i+1, j), (i+1, j+1)]
		sur = [(i[0], i[1]) for i in sur if -1 < i[0] < 8 and -1 < i[1] < 8]
		return sur 

	def check_move(self, end_position,Chess_Board):
		if not self.poss_moves:
			return False

		cur_position = self.get_position()
		cur_Board = Chess_Board.get_positions()
		sur = self.get_sourrounding()

		if end_position not in sur:
			return False

		if end_position not in cur_Board:
			return True

		if end_position in cur_Board and cur_Board[end_position]._color != self._color:
			return True

		return False

	def update_current_pos(self, new_position):
		self.position = new_position

	def update_poss_moves(self,Chess_Board):
		sur = self.get_sourrounding()
		cur_Board = Chess_Board.get_positions()
		self.poss_moves = [(i[0], i[1]) for i in sur if i not in cur_Board or Chess_Board.Fig_Pos[(i[0], i[1])]._color != self._color]


class Queen(Figure):
	def __init__(self, color, position, poss_moves, figure = 'Queen'):
		Figure.__init__(self, color, position, poss_moves)
		self._figure = figure

	def get_sourrounding(self,Chess_Board):
		cur_Board = Chess_Board.get_positions()
		i,j = self.position[0], self.position[1]
		sur = []
		for count, m in enumerate([(i+1, 8, 1), (i-1, -1, -1), (j+1, 8, 1), (j-1, -1, -1)]):
			for k in range(m[0], m[1], m[2]):
				udrl = (k,j) if count < 2 else (i,k)
				if udrl not in cur_Board: 
					sur.append(udrl)
				elif udrl in cur_Board and Chess_Board.Fig_Pos[udrl]._color != self._color:
					sur.append(udrl)
					break
				else:
					break

		for pos in ([1, 1], [1, -1], [-1, 1], [-1, -1]):
			i_m = pos[0]
			j_m = pos[1]
			while -1 < i+i_m < 8 and -1 < j+j_m < 8:
				if (i+i_m, j+j_m) in cur_Board and Chess_Board.Fig_Pos[(i+i_m, j+j_m)]._color != self._color:
					sur.append((i+i_m, j+j_m))
					break
				elif (i+i_m, j+j_m) in cur_Board and Chess_Board.Fig_Pos[(i+i_m, j+j_m)]._color == self._color:
					break
				else:
					sur.append((i+i_m, j+j_m))
					i_m += pos[0]
					j_m += pos[1]
		return sur

	def update_poss_moves(self,Chess_Board):
		self.poss_moves = self.get_sourrounding(Chess_Board)


class Bishop(Figure):
	def __init__(self, color, position, poss_moves, figure = 'Bishop'):
		Figure.__init__(self, color, position, poss_moves)
		self._figure = figure

	def get_sourrounding(self,Chess_Board):
		cur_Board = Chess_Board.get_positions()
		i,j = self.position[0], self.position[1]
		sur = []
		for pos in ([1, 1], [1, -1], [-1, 1], [-1, -1]):
			i_m = pos[0]
			j_m = pos[1]
			while -1 < i+i_m < 8 and -1 < j+j_m < 8:
				if (i+i_m, j+j_m) in cur_Board and Chess_Board.Fig_Pos[(i+i_m, j+j_m)]._color != self._color:
					sur.append((i+i_m, j+j_m))
					break
				elif (i+i_m, j+j_m) in cur_Board and Chess_Board.Fig_Pos[(i+i_m, j+j_m)]._color == self._color:
					break
				else:
					sur.append((i+i_m, j+j_m))
					i_m += pos[0]
					j_m += pos[1]
		return sur		

	def update_poss_moves(self,Chess_Board):
		self.poss_moves = self.get_sourrounding(Chess_Board)


class Rook(Figure):
	def __init__(self, color, position, poss_moves, figure = 'Rook'):
		Figure.__init__(self, color, position, poss_moves)
		self._figure = figure
		self.already_moved = False

	def get_sourrounding(self,Chess_Board):
		cur_Board = Chess_Board.get_positions()
		i,j = self.position[0], self.position[1]
		sur = []
		for count, m in enumerate([(i+1, 8, 1), (i-1, -1, -1), (j+1, 8, 1), (j-1, -1, -1)]):
			for k in range(m[0], m[1], m[2]):
				udrl = (k,j) if count < 2 else (i,k)
				if udrl not in cur_Board: 
					sur.append(udrl)
				elif udrl in cur_Board and Chess_Board.Fig_Pos[udrl]._color != self._color:
					sur.append(udrl)
					break
				else:
					break
		return sur

	def update_poss_moves(self,Chess_Board):
		self.poss_moves = self.get_sourrounding(Chess_Board)


class Knight(Figure):
	def __init__(self, color, position, poss_moves, figure = 'Knight'):
		Figure.__init__(self, color, position, poss_moves)
		self._figure = figure

	def get_sourrounding(self,Chess_Board):
		sur = []
		cur_Board = Chess_Board.get_positions()
		i = self.position[0]
		j = self.position[1]

		for posspos in [(i-2, j-1), (i-2, j+1), (i-1, j-2), (i-1, j+2), (i+2, j-1), (i+2, j+1), (i+1, j-2), (i+1, j+2)]:
			i_k = posspos[0]
			j_k = posspos[1]
			if 0 <= i_k < 8 and 0 <= j_k < 8 and (i_k, j_k) not in cur_Board:
				sur.append((i_k, j_k))
			if 0 <= i_k < 8 and 0 <= j_k < 8 and (i_k, j_k) in cur_Board and Chess_Board.Fig_Pos[(i_k, j_k)]._color != self._color:
				sur.append((i_k, j_k))	
		return sur

	def update_poss_moves(self,Chess_Board):
		self.poss_moves = self.get_sourrounding(Chess_Board)


class Pawn(Figure):
	def __init__(self, color, position, poss_moves, figure = 'Pawn'):
		Figure.__init__(self, color, position, poss_moves)
		self._figure = figure

	def get_sourrounding(self,Chess_Board):
		sur = []
		cur_Board = Chess_Board.get_positions()
		i = self.position[0]
		j = self.position[1]

		if self._color == 0:
			if (i+1, j) not in cur_Board:
				sur.append((i+1, j))
				if i == 1 and (i+2, j) not in cur_Board: 
					sur.append((i+2, j))			
			if (i+1, j+1) in cur_Board and cur_Board[(i+1, j+1)]._color != 0:
				sur.append((i+1, j+1))
			if (i+1, j-1) in cur_Board and cur_Board[(i+1, j-1)]._color != 0:
				sur.append((i+1, j-1))
		else:
			if (i-1, j) not in cur_Board:
				sur.append((i-1, j))
				if i == 6 and (i-2, j) not in cur_Board: 
					sur.append((i-2, j))			
			if (i-1, j+1) in cur_Board and cur_Board[(i-1, j+1)]._color != 1:
				sur.append((i-1, j+1))
			if (i-1, j-1) in cur_Board and cur_Board[(i-1, j-1)]._color != 1:
				sur.append((i-1, j-1))			
		return sur

	def update_poss_moves(self,Chess_Board):
		self.poss_moves = self.get_sourrounding(Chess_Board)	


def check_if_move_is_possible(start_position, end_position,Chess_Board):
	print("STARTING POSITION: ", start_position, " ENDING POSITION: ", end_position)
	print('first check...')
	cur_Board = Chess_Board.get_positions()
	print(Chess_Board.Fig_Pos[(start_position)]._color, Chess_Board.Fig_Pos[(start_position)]._figure, Chess_Board.Fig_Pos[(start_position)].poss_moves)
	if end_position in Chess_Board.Fig_Pos[(start_position)].poss_moves:
		return True
	else:
		return False


def check_if_own_king_in_danger(start_position, end_position,Chess_Board):
	print('second check...')
	current_color = Chess_Board.Fig_Pos[start_position]._color
	position_own_king = ()

	print("here1")
	Chess_Board.Fig_Pos[start_position].position = end_position
	print("here2")
	Chess_Board.update_positions(start_position, end_position)
	print("here")
	for to_update in Chess_Board.Fig_Pos:
		Chess_Board.Fig_Pos[to_update].update_poss_moves(Chess_Board)
		if Chess_Board.Fig_Pos[to_update]._figure == 'King' and Chess_Board.Fig_Pos[to_update]._color == current_color:
			position_own_king = Chess_Board.Fig_Pos[to_update].position
	
	print('test6')
	for figures in Chess_Board.Fig_Pos:
		if Chess_Board.Fig_Pos[figures]._color != current_color and position_own_king in Chess_Board.Fig_Pos[figures].poss_moves:
			print('Move not possible. Own King would be in check')
			Chess_Board.Fig_Pos[end_position].position = start_position
			Chess_Board.update_positions(end_position, start_position)
			for to_update in Chess_Board.Fig_Pos:
				Chess_Board.Fig_Pos[to_update].update_poss_moves(Chess_Board)	
			return False
	print('test7')
	return True


def check_if_checkmate(current_color, start_position, end_position,Chess_Board):
	enemy_king_pos = ()

	for find_king in Chess_Board.Fig_Pos:
		if Chess_Board.Fig_Pos[find_king]._figure == 'King' and Chess_Board.Fig_Pos[find_king]._color != current_color:
			enemy_king_pos = Chess_Board.Fig_Pos[find_king].position

	who_attacks = []
	attackers_moves = []

	print('test9')
	for find_attacker in Chess_Board.Fig_Pos:
		if Chess_Board.Fig_Pos[find_attacker]._color == current_color and enemy_king_pos in Chess_Board.Fig_Pos[find_attacker].poss_moves:
			who_attacks.append(Chess_Board.Fig_Pos[find_attacker].position)
			attackers_moves.extend(Chess_Board.Fig_Pos[find_attacker].poss_moves)
	print('test10')
	if not who_attacks:
		print('test11')
		return True

	for find_helpers in Chess_Board.Fig_Pos:
		print("helpers are ", find_helpers)			

	print("am",attackers_moves)
	print("kms", Chess_Board.Fig_Pos[enemy_king_pos].poss_moves)
	for king_move in Chess_Board.Fig_Pos[enemy_king_pos].poss_moves:
		if king_move not in attackers_moves:
			print('check!')
			return True

	print('check mate!')
	global playing
	playing = False
	return False


def check_rochade(current_color, start_position, end_position,Chess_Board):
	print('test')

	cur_Board = Chess_Board.get_positions()
	if start_position not in cur_Board or end_position not in cur_Board:
		print("first here")
		return False
	p1 = cur_Board[start_position]
	p2 = cur_Board[end_position]
	p1_position = p1.position
	p2_position = p2.position

	if p1._color != p2._color or p1._figure not in ('King', 'Rook') or p2._figure not in ('King', 'Rook'):
		print("here test")
		return False

	if p1.already_moved or p2.already_moved:
		print('Figures already moved.')
		return False

	print('test2')
	pos_between = []
	if p1.position == (0,0) or p2.position == (0,0):
		pos_between = [(0,1), (0,2), (0,3)]
	elif p1.position == (0,7) or p2.position == (0,7):
		pos_between = [(0,5), (0,6)]
	elif p1.position == (7,0) or p2.position == (7,0):
		pos_between = [(7,1), (7,2), (7,3)]
	elif p1.position == (7,7) or p2.position == (7,7):
		pos_between = [(7,5), (7,6)]

	print(pos_between)
	for check_poss_attack in Chess_Board.Fig_Pos:
		if Chess_Board.Fig_Pos[check_poss_attack]._color != current_color:
			for positions_between in pos_between:
				if positions_between in Chess_Board.Fig_Pos[check_poss_attack].poss_moves:
					print('test5')
					return False

	print('test3')
	Chess_Board.Fig_Pos[start_position].position = end_position
	Chess_Board.Fig_Pos[end_position].position = start_position
	Chess_Board.update_position_rochade(start_position, end_position)

	for to_update in Chess_Board.Fig_Pos:
		Chess_Board.Fig_Pos[to_update].update_poss_moves(Chess_Board)

	position_own_king = ()
	for to_update in Chess_Board.Fig_Pos:
		if Chess_Board.Fig_Pos[to_update]._figure == 'King' and Chess_Board.Fig_Pos[to_update]._color == current_color:
			position_own_king = Chess_Board.Fig_Pos[to_update].position

	for figures in Chess_Board.Fig_Pos:
		if Chess_Board.Fig_Pos[figures]._color != current_color and position_own_king in Chess_Board.Fig_Pos[figures].poss_moves:	
			Chess_Board.Fig_Pos[end_position].position = start_position
			Chess_Board.Fig_Pos[start_position].position = end_position
			Chess_Board.update_position_rochade(end_position, start_position)

			for to_update in Chess_Board.Fig_Pos:
				Chess_Board.Fig_Pos[to_update].update_poss_moves(Chess_Board)			
			return False 
	p1.already_moved = True
	p2.already_moved = True
	return True