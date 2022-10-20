# Tic-Tac-Toe game 

The code contains 5 main functions:

Relied on using Python lists, dictionaries, loops, functions, and modules (random)
The code consisted of five main functions:
  1. display_board: used to draw the tic-tac-toe board between turns
  2. enter_move: used to enter the player's turn to place the "O", uses a dictionary to assign square numbers on the board to tuple pairs, translating the location of     where the player selects to play the "O"
  3. make_list_of_free_fields: used to check free squares on the tic-tac-toe board
  4. victory_for: used to check if either the player or computer won the game
  5. draw_move: used to simulate the computer's turn to place the "X", the computer checks the free squares before using .choice() method from random module to randomly select an empty square on the board to place the "X"
The while loop iterates over the number of squares and terminates if the player/computer won the game before filling all squares
The game asks the user if they would like to play first and uses module operation to determine the turns
