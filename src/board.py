
from settings import *
from ship import Ship  # Подключение класс Корабль


# ---------------------------------------------------------------------------------

# Функция возращает список кораблей
# для каждого коробля, для каждой доски 
def create_ships(w, h):
	return [
		[Ship(SIZE_SMALL , w, h) for _ in range(NUMBER_SMALL )], # Маленькие корабли
		[Ship(SIZE_MEDIUM, w, h) for _ in range(NUMBER_MEDIUM)], # Средние корабли
		[Ship(SIZE_LARGE , w, h) for _ in range(NUMBER_LARGE )]  # Большие корабли
	]


class Board:
	def __init__(self, w, h):
		self.w, self.h = w, h # Ширина, Высота доски

		self.number_hit_enemy  = 0 # количество пораженных врагов
		self.number_hit_player = 0 # количество пораженных игроков
		self.number_ships = 8 # Количество кораблей

		# Создаю список из точек короблй
		self.ships_enemy  = create_ships(self.w, self.h) # Корабля врага
		self.ships_player = create_ships(self.w, self.h) # Корабля Игрока

		# self.board_old_enemy -> Нужен для выполнения игровых действий и расположение кораблей
		self.board_old_enemy = [[EMPYT for _ in range(self.w)] for _ in range(self.h)]
		self.board_new_enemy = [[EMPYT for _ in range(self.w)] for _ in range(self.h)] # self.board_new_enemy -> Для отображения атак игрока
		self.board_old_enemy = self.arrange_ships(self.ships_enemy, self.board_old_enemy) # self.board_old_enemy -> Заполним доску кораблями

		# self.board_old_player -> Нужен для выполнения игровых действий и расположение кораблей
		self.board_old_player = [[EMPYT for _ in range(self.w)] for _ in range(self.h)]
		self.board_old_player = self.arrange_ships(self.ships_player, self.board_old_player) # self.board_old_player -> Заполним доску кораблями


	# расстановка кораблей
	def arrange_ships(self, list_ships, board):
		for ships in list_ships: # берем список всех кораблей (все размеры)
			for ship in ships: # берем список всех кораблей (последовательно Маленькие, Средние, Большие)
				points = ship.start_loc(board) # получение позиция кораблей
				for loc in points: # расставляем корабли по местам
					board[loc[1]][loc[0]] = SHIP
		
		return board # Возращает иговую доску заполненую кораблями 


	# Обновление игровой доски
	def update(self, step, x, y):
		if step == STEP_PL: # Ход игрока
			x, y = x - 1, y - 1
			# Пустая клетка врага, промах
			if self.board_old_enemy[x][y] == EMPYT: 
				self.board_new_enemy[x][y] = MISSES
			# Клетка корабля, попадание
			elif self.board_old_enemy[x][y] == SHIP: 
				self.board_new_enemy[x][y] = DAMAGED
				self.number_hit_player += 1 # количество пораженных игроков
			return STEP_EN # ходит враг

		elif step == STEP_EN: # Ход врага
			x, y = x - 1, y - 1
			# Пустая клетка грока, промах
			if self.board_old_player[x][y] == EMPYT: 
				self.board_old_player[x][y] = MISSES
			# Клетка корабля, попадание
			elif self.board_old_player[x][y] == SHIP: 
				self.board_old_player[x][y] = DAMAGED
				self.number_hit_enemy += 1 # количество пораженных врагов
			return STEP_PL # ходит игрока


	def draw(self, title, board):
		print(f"  Board {title} ") # Название доски
		print( end='  ' ) # end='  ' -> Заменяем перенос строки(\n) на пробелы('  ')
		[print( f'{i + 1}', end=' ' ) for i in range(self.w)] # Пронумеровываем столбци
		print() # Перенос строки(\n)

		for i in range(self.h): # Высота, количество строк
			print( i + 1, end='|' ) # Нумерация строки и закрытие ее знаком |
			for j in range(self.w): # Ширина, количество столбцов
				print( board[i][j], end='|' ) # Отображение элемента клетки и заменяем перенос строки(\n) на пробелы('|')
			print() # Перенос строки(\n)

