import random

PLAYER = 'X'
BOT = 'O'
EMPTY = ' '

def print_board(board):
    print("\n")
    print(f"     {board[6]} | {board[7]} | {board[8]}  ")
    print("    -----------")
    print(f"     {board[3]} | {board[4]} | {board[5]}  ")
    print("    -----------")
    print(f"     {board[0]} | {board[1]} | {board[2]}  ")
    print("\n")

def check_win(board, player):
    win_combinations = [
        [6, 7, 8], [3, 4, 5], [0, 1, 2],  #горизонтали
        [6, 3, 0], [7, 4, 1], [8, 5, 2],  #вертикали
        [6, 4, 2], [8, 4, 0]              #диагонали
    ]
    return any(all(board[i] == player for i in combo) for combo in win_combinations)

def is_board_full(board):
    return all(cell != EMPTY for cell in board)

def get_player_move(board):
    while True:
        try:
            move = int(input("Выберите клетку (1-9): ")) - 1
            if 0 <= move <= 8 and board[move] == EMPTY:
                return move
            print("Некорректный ход. Попробуйте еще раз.")
        except ValueError:
            print("Введите число от 1 до 9!")

def find_best_move(board):
    #Проверка может ли бот выиграть
    for i in range(9):
        if board[i] == EMPTY:
            board[i] = BOT
            if check_win(board, BOT):
                board[i] = EMPTY
                return i
            board[i] = EMPTY
    
    #Блокировка игрока
    for i in range(9):
        if board[i] == EMPTY:
            board[i] = PLAYER
            if check_win(board, PLAYER):
                board[i] = EMPTY
                return i
            board[i] = EMPTY
    
    #Выбор случайной свободной клетки
    empty_cells = [i for i, cell in enumerate(board) if cell == EMPTY]
    return random.choice(empty_cells)

def main():
    board = [EMPTY] * 9
    current_player = PLAYER
    
    print("\nДобро пожаловать в игру Крестики-Нолики!")
    print(f"Вы играете за {PLAYER}, бот играет за {BOT}")
    print("Нумерация клеток:")
    print("""
      7 | 8 | 9  
    ------------
      4 | 5 | 6  
    ------------
      1 | 2 | 3  
    """)
    
    while True:
        print_board(board)
        
        if current_player == PLAYER:
            move = get_player_move(board)
            board[move] = PLAYER
        else:
            print("Ход бота...")
            move = find_best_move(board)
            board[move] = BOT
        
        if check_win(board, current_player):
            print_board(board)
            print("🎉 Поздравляю! Вы победили!" if current_player == PLAYER else "😢 Бот победил!")
            break
        
        if is_board_full(board):
            print_board(board)
            print("🤝 Ничья!")
            break
        
        current_player = BOT if current_player == PLAYER else PLAYER
    
    if input("Хотите сыграть еще раз? (да/нет): ").lower() == 'да':
        main()
    else:
        print("Спасибо за игру!")

if __name__ == "__main__":
    main()
