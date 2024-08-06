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

# coins_players_map = {
#     '00': 0,
#     '11': 1,
#     '22': 2
# }

# %%
class Connect4_board:
    def __init__(self, player_1, player_2) -> None:
        self.__os_type = platform.system()
        self.__rows_no = 6
        self.__column_no = 7
        self.__board = np.zeros((self.__rows_no, self.__column_no))
        # self.__board[0, :] = 1
        # self.__board[1, :] = 2
        # self.__board[2, :] = 1
        # self.__board[3, :] = 2
        # self.__board[4, :] = 1
        # self.__board[5, :] = 2
        self.__player_1 = player_1
        self.__player_2 = player_2

    def clear_console(self) -> None:
        """
            clear_console: is used to clear console ground.
                os_type(string): type of operating system where code run in.
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
                board += f'   {colored('  ', *(players_coins_map[int(self.__board[row, col])]))}   |'

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
        pass
    
    def __is_legal_play(self, column_no):
        """
            __is_legal_play: is used to check if ther is an empty space on the column that player choose to play.  
        """
        column = self.__board[:, column_no]
        return column.min() == 0
    
    def add_coin(self, player_id, column_no):
        """
            add_coin: is used to allow the player to add coin on the board.  
        """
        if self.__is_legal_play(column_no):
            column = self.__board[:, column_no]
            unique, counts = np.unique(column, return_counts=True)
            zero_count = dict(zip(unique, counts))[0]
            self.__board[(zero_count - 1), column_no] = player_id

# %%
board_env = Connect4_board(None, None)
board_env.clear_console()
board_env.print_board()

board_env.add_coin(1, 3)
time.sleep(3)
board_env.clear_console()
board_env.print_board()

board_env.add_coin(1, 3)
time.sleep(3)
board_env.clear_console()
board_env.print_board()

board_env.add_coin(1, 3)
time.sleep(3)
board_env.clear_console()
board_env.print_board()






