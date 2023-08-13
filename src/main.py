
from settings import * # Импортирую настройки(Постоянные переменные)
from board import Board # Подключение класс Доска

import os, random # Импортирую системный модуль и модуль рандома


# ---------------------------------------------------------------------------------

def main():
	board = Board(BOARD_WIDTH, BOARD_HEIGHT) # Создания доски
	step = STEP_PL  # Создание шага
	action = [1, 1] # Определяем список координат

	while True:
		os.system("cls") # Очистка консоли

		board.draw(STEP_EN, board.board_new_enemy)  # Отрисовка доски врага
		board.draw(STEP_PL, board.board_old_player) # Отрисовка доски игрока

		# Проигрыш если враг зарвет ваши корабли быстрее
		if board.number_hit_enemy >= board.number_ships: print("You Failed"); break
		# Выша победа если вы набереде board.number_hit_player больше врага
		if board.number_hit_player >= board.number_ships: print("You Win"); break

		# Шаг игрока
		if step == STEP_PL:
			# Цикл для повторения попытки ввода данных
			# если вы введете неправильные данные
			while True:
				action = input("Enter the position X and Y:") # Вводимые данные
				if action == 'q': break # Конец игры

				# Исключения ошибки при неправильных данных
				# int(action.split(' ')[0/1]) -> расщеплять текст в список и получение элемента по индексу
				try: x, y = int(action.split(' ')[0]), int(action.split(' ')[1])
				except Exception: continue # Возрат к началу цикла при ошибке

				# Возрат к началу цикла при выходе за гроници списка
				if x > BOARD_WIDTH or y > BOARD_HEIGHT: continue
				# Возврат к началу цикла при попадании по знаку T - misses и X - damaged
				elif board.board_new_enemy[y - 1][x - 1] in (MISSES, DAMAGED): continue
				# Выход из цикла когда все условия выше не выполняются
				else: action = [x, y]; break

		# Шаг врага
		elif step == STEP_EN:
			# Цикл для получения лучшей точки для удара
			while True:
				x = random.randint(1, BOARD_WIDTH)  # Рандомное координата по X
				y = random.randint(1, BOARD_HEIGHT) # Рандомное координата по Y

				# Возврат к началу цикла при попадании по знаку T - misses и X - damaged
				if board.board_old_player[y - 1][x - 1] in (MISSES, DAMAGED): continue
				# Выход из цикла когда все условия выше не выполняются
				else: action = [x, y]; break

		if action == 'q': break # Конец игры

		# Обновление данных в зависимости кто ходит и позиций
		# Возвращает имя того кто должен идти следующим
		step = board.update(step, action[1], action[0])


# ---------------------------------------------------------------------------------

if __name__ == '__main__':
	main() # Запуск игры
	quit() # Закрытие программы

