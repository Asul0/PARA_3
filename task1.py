def display_board(board):
    for i in range(0, 9, 3):
        print(f"{board[i]} | {board[i + 1]} | {board[i + 2]}")
        if i < 6:
            print("---------")

def check_winner(board, player):
    # Проверка по горизонтали, вертикали и диагоналям
    for i in range(0, 3):
        if all(board[i] == player for i in range(i, 9, 3)) or \
           all(board[i] == player for i in range(3*i, 3*i + 3)) or \
           (board[0] == board[4] == board[8] == player) or \
           (board[2] == board[4] == board[6] == player):
            return True
    return False

def is_board_full(board):
    return all(cell != ' ' for cell in board)

def tic_tac_toe():
    board = [' '] * 9
    current_player = 'X'

    while True:
        display_board(board)
        move = int(input(f"Игрок {current_player}, введите номер ячейки (1-9): ")) - 1

        if 0 <= move < 9 and board[move] == ' ':
            board[move] = current_player

            if check_winner(board, current_player):
                display_board(board)
                print(f"Игрок {current_player} победил!")
                break

            if is_board_full(board):
                display_board(board)
                print("Ничья!")
                break

            current_player = 'O' if current_player == 'X' else 'X'
        else:
            print("Некорректный ход. Попробуйте еще раз.")

if __name__ == "__main__":
    tic_tac_toe()
