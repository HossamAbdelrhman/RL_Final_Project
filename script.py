# %%
# install all required libs
## ! pip install tensorflow
# ! pip install numpy
# ! pip install tabulate
# ! pip install termcolor

# python virsion must be >3.10

# %%
# import required libs
import os
import time
import platform
import numpy as np
from enum import Enum
from tabulate import tabulate
from termcolor import colored
# import tensorflow as tf

# %%
"""

|       |       |       |       |       |       |       |
|       |       |       |       |       |       |       |
|       |       |       |       |       |       |       |
---------------------------------------------------------
|       |       |       |       |       |       |       |
|       |       |       |       |       |       |       |
|       |       |       |       |       |       |       |
---------------------------------------------------------
|       |       |       |       |       |       |       |
|       |       |       |       |       |       |       |
|       |       |       |       |       |       |       |
---------------------------------------------------------
|       |       |       |       |       |       |       |
|       |       |       |       |       |       |       |
|       |       |       |       |       |       |       |
---------------------------------------------------------
|       |       |       |       |       |       |       |
|       |       |       |       |       |       |       |
|       |       |       |       |       |       |       |
---------------------------------------------------------
|       |       |       |       |       |       |       |
|       |       |       |       |       |       |       |
|       |       |       |       |       |       |       |
---------------------------------------------------------
|   A   |   B   |   C   |   D   |   E   |   F   |   G   |
---------------------------------------------------------
"""
       

# %%
players_coins_map = {
    0: [],
    1: ['red', 'on_red'],
    2: ['yellow', 'on_yellow']
}

column_index_to_number_map = {
    'A': 0,
    'B': 1,
    'C': 2,
    'D': 3,
    'E': 4,
    'F': 5,
    'G': 6
}

# %%
class Connect4_board:
    def __init__(self, player_1, player_2) -> None:
        self.__os_type = platform.system()
        self.__rows_no = 6
        self.__column_no = 7
        self.__board = np.zeros((self.__rows_no, self.__column_no))
        self.__player_1 = player_1
        self.__player_2 = player_2
        self.__current_player = np.random.choice([self.__player_1, self.__player_2])

    def clear_console(self) -> None:
        """
            clear_console: is used to clear console ground.
        """
        os_type = self.__os_type
        match os_type:
            case 'Windows':
                os.system('cls')
            case 'Linux':
                os.system('clear')

    def __build_board(self) -> str:
        board = ''
        for row in range(self.__rows_no):
            board += f"\n|        |        |        |        |        |        |        |"
            board += f"\n|"
            for col in range(self.__column_no):
                board += f"   {colored('  ', *(players_coins_map[int(self.__board[row, col])]))}   |"

            board += f"\n|        |        |        |        |        |        |        |"
            board += "\n"
            board += "----------------------------------------------------------------"
        
        board += "\n|   A    |   B    |   C    |   D    |   E    |   F    |   G    |\n"
        board += "----------------------------------------------------------------"

        return board

    def print_board(self) -> None:
        """
            print_board: is used to print connect 4 board in console.  
        """
        print(self.__build_board())
        
    def check_win(self, player_id):
        board = self.__board
        rows, columns = board.shape

        # Check horizontally
        for i in range(rows):
            for j in range(columns - 3):
                if(
                    board[-i-1, j]==player_id and
                    board[-i-1, j+1]==player_id and
                    board[-i-1, j+2]==player_id and
                    board[-i-1, j+3]==player_id
                ):
                    return True
                
        # Check vertically
        for j in range(columns):
            for i in range(rows-3):
                if(
                    board[-i-1, j]==player_id and
                board[-i-2, j]==player_id and
                board[-i-3, j]==player_id and
                board[-i-4, j]==player_id
                ):
                    return True
                
        # Check main diagonal (top-left to bottom-right)
        for i in range(rows-3):
            for j in range(columns - 3):
                if(
                    board[i, j]==player_id and
                    board[i+1, j+1]==player_id and
                    board[i+2, j+2]==player_id and
                    board[i+3, j+3]==player_id 
                ):
                    return True
                
        # Check secondary diagonal (top-right to bottom-left)
        for i in range(rows-3):
            for j in range(-1, 2-columns, -1):
                if(
                    board[i, j]==player_id and
                    board[i+1, j-1]==player_id and
                    board[i+2, j-2]==player_id and
                    board[i+3, j-3]==player_id 
                ):
                    return True

        return False
    
    def __is_legal_play(self, column_no):
        """
            __is_legal_play: is used to check if ther is an empty space on the column that player choose to play.
                column_no (int): represent the numerical index equavilant value. 
        """
        column = self.__board[:, column_no]
        return column.min() == 0
    
    def add_coin(self, player_id, column_no):
        """
            add_coin: is used to allow the player to add coin on the board.  
            player_id (int): represent the id of the player.
            column_no (int): represent the numerical index equavilant value.
        """
        if self.__is_legal_play(column_no):
            column = self.__board[:, column_no]
            unique, counts = np.unique(column, return_counts=True)
            zero_count = dict(zip(unique, counts))[0]
            self.__board[(zero_count - 1), column_no] = player_id

    ########################################################
    
    def reset(self):
        self.__board = np.zeros((self.__rows_no, self.__column_no))

    def get_reword(self):
        pass

    def step(self, action):
        ## apply action then calculate the the reword
        return self.get_reword(), self.check_win()
    
    def flip_flop_current_players():
        pass

# %%
inds = ['A', 'B', 'C', 'E', 'F', 'G']
is_win = False

board_env = Connect4_board(None, None)
board_env.clear_console()
board_env.print_board()

while not is_win:
    board_env.add_coin(1, 3)
    time.sleep(2.5)
    board_env.clear_console()
    board_env.print_board()
    is_win = board_env.check_win(1)
    print(f'Is player (1) win: {is_win}')
    
    if(not is_win):
        player_2_random_choise = np.random.choice(inds)
        board_env.add_coin(2, column_index_to_number_map[player_2_random_choise])
        time.sleep(2.5)
        board_env.clear_console()
        board_env.print_board()
        is_win = board_env.check_win(2)
        print(f'Is player (2) win: {is_win}')



# %%
# test = np.zeros((3, 6))
# col_3 = test[:, 2]
# print(col_3.min() == 0)

# %%
# def check_consecutive(board:np.array, player_id:int):
#     rows, columns = board.shape

#     # Check horizontally
#     for i in range(rows):
#         for j in range(columns - 3):
#             if(
#                 board[-i-1, j]==player_id and
#                 board[-i-1, j+1]==player_id and
#                 board[-i-1, j+2]==player_id and
#                 board[-i-1, j+3]==player_id
#             ):
#                 return True
            
#     # Check vertically
#     for j in range(columns):
#         for i in range(rows-3):
#             if(
#                 board[-i-1, j]==player_id and
#                board[-i-2, j]==player_id and
#                board[-i-3, j]==player_id and
#                board[-i-4, j]==player_id
#             ):
#                 return True
            
#     # Check main diagonal (top-left to bottom-right)
#     for i in range(rows-3):
#         for j in range(columns - 3):
#             if(
#                 board[i, j]==player_id and
#                 board[i+1, j+1]==player_id and
#                 board[i+2, j+2]==player_id and
#                 board[i+3, j+3]==player_id 
#             ):
#                 return True
            
#     # Check secondary diagonal (top-right to bottom-left)
#     for i in range(rows-3):
#         for j in range(-1, 2-columns, -1):
#             if(
#                 board[i, j]==player_id and
#                 board[i+1, j-1]==player_id and
#                 board[i+2, j-2]==player_id and
#                 board[i+3, j-3]==player_id 
#             ):
#                 return True

#     return False

# # Example usage
# matrix = [
#     [2, 0, 0, 2, 2, 0, 0],
#     [1, 2, 0, 0, 2, 2, 1],
#     [2, 1, 2, 0, 2, 2, 2],
#     [1, 2, 1, 1, 2, 12, 1],
#     [1, 1, 2, 2, 2, 0, 0],
#     [1, 2, 0, 2, 0, 2, 2]
# ]

# value_to_check = 2

# result = check_consecutive(np.array(matrix), value_to_check)
# if result:
#     print(f"{value_to_check} win.")
# else:
#     print(f"{value_to_check} does not win.")


# %%


# %%



