#dungeon_game.py

import random
import os

# draw grid
# pick random location for player
# pick random location for exit door
# pick random location for the monster
# draw player in the grid
# take input for movement
# move player, unless invalid move (past edges or grid)
# check for win/loss
# clear screen and redraw grid

CELLS = [ (0,0), (1,1), (2,0), (3,0), (4,0),
		  (0,1), (1,2), (2,1), (3,1), (4,1),
		  (0,2), (1,3), (2,2), (3,2), (4,2),
		  (0,3), (1,4), (2,3), (3,3), (4,3),
		  (0,4), (1,5), (2,4), (3,4), (4,4)]

def clear_scree():
	os.system('cls' if os.name == 'nt' else 'clear')

def get_locations():
	return random.sample(CELLS, 3)

	#REPLACED WITH ABOVE 
	# monster = None
	# door = None
	# player = None

	# monster = random.sample(CELLS, 2)
	# door = random.sample(CELLS, 2)
	# player = random.sample(CELLS, 2)

	# return monster, door, player

def move_player(player, move):
	# get the player's position
	# if move == LEFT, x-1
	# if move == RIGHT, x+1
	# if move == UP, y-1
	# if move == DOWN, y+1
	return player

def get_moves(player):
	moves = ["LEFT", "RIGHT", "UP", "DOWN"]
	# if player's y == 0, they can't move up
	# if player's y == 4, they can't move down
	# if player's x == 0, they can't move left
	# if player's x == 4, they can't move right
	x,y = player
	if x == 0:
		moves.remove("LEFT")
	if x == 4:
		moves.remove("RIGHT")
	if y == 0:
		moves.remove("UP")
	if y == 4:
		moves.remove("DOWN")
	return moves

#unpacking into vars works with lists too, can be in any order
monster, door, player = get_locations()

while True:
	print("Welcome to the Dungeon!")
	print("You're currently in room {}".format(player))  # fill with player position
	print("YOu can move {}".format(", ".join(get_moves(player))))  # fill with available move
	print("Enter QUIT to quit")

	move = input("> ")
	move = move.upper()

	if move == 'QUIT':
		break

	# Good move? Change the player position
	# Bad move? Don't change anything!
	# On the door? The win!
	# On the monster? The lose!
	# Otherwise, loop back around

