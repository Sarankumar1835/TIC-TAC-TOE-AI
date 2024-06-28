#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np

def create_board():
    return np.zeros((3, 3), dtype=int)

def display_board(board):
    for row in board:
        print(' | '.join(str(cell) for cell in row))
        print('-' * 5)

def check_winner(board):
    for i in range(3):
        if np.all(board[i, :] == 1) or np.all(board[:, i] == 1):
            return 1
        if np.all(board[i, :] == 2) or np.all(board[:, i] == 2):
            return 2
    if np.all(board.diagonal() == 1) or np.all(np.fliplr(board).diagonal() == 1):
        return 1
    if np.all(board.diagonal() == 2) or np.all(np.fliplr(board).diagonal() == 2):
        return 2
    if np.all(board != 0):
        return 0
    return -1

def is_moves_left(board):
    return np.any(board == 0)
def minimax(board, depth, is_maximizing):
    score = check_winner(board)
    if score == 1:
        return -10
    if score == 2:
        return 10
    if score == 0:
        return 0

    if is_maximizing:
        best = -1000
        for i in range(3):
            for j in range(3):
                if board[i][j] == 0:
                    board[i][j] = 2
                    best = max(best, minimax(board, depth + 1, not is_maximizing))
                    board[i][j] = 0
        return best
    else:
        best = 1000
        for i in range(3):
            for j in range(3):
                if board[i][j] == 0:
                    board[i][j] = 1
                    best = min(best, minimax(board, depth + 1, not is_maximizing))
                    board[i][j] = 0
        return best
def find_best_move(board):
    best_val = -1000
    best_move = (-1, -1)
    for i in range(3):
        for j in range(3):
            if board[i][j] == 0:
                board[i][j] = 2
                move_val = minimax(board, 0, False)
                board[i][j] = 0
                if move_val > best_val:
                    best_move = (i, j)
                    best_val = move_val
    return best_move
def play_game():
    board = create_board()
    human_turn = True
    while True:
        display_board(board)
        winner = check_winner(board)
        if winner != -1:
            if winner == 1:
                print("Human wins!")
            elif winner == 2:
                print("AI wins!")
            else:
                print("It's a tie!")
            break
        if human_turn:
            row, col = map(int, input("Enter row and column (0, 1, or 2): ").split())
            if board[row][col] == 0:
                board[row][col] = 1
                human_turn = False
            else:
                print("Invalid move. Try again.")
        else:
            print("AI's turn.")
            move = find_best_move(board)
            board[move[0]][move[1]] = 2
            human_turn = True

play_game()


# In[ ]:




