# Our game's player only has two attributes, x and y coordinates. Let's practice with a slightly different one, 
# though. This one has x, y, and "hp", which stands for hit points.

# Our move function takes this three-part tuple player and a direction tuple that's two parts, the x to move 
# and the y (like (-1, 0) would move to the left but not up or down).

# Finish the function so that if the player is being run into a wall, their hp is reduced by 5. Don't let them 
# go past the wall. Consider the grid to be 0-9 in both directions. Don't worry about keeping their hp above 0 either.

# EXAMPLES:
# move((1, 1, 10), (-1, 0)) => (0, 1, 10)
# move((0, 1, 10), (-1, 0)) => (0, 1, 5)
# move((0, 9, 5), (0, 1)) => (0, 9, 0)



def move(player, direction): 
	x, y, hp = player
	print("Player info X:{},Y:{},HP:{}".format(x, y, hp)) 
	a, b = direction 
	print("Wants to move X:{},Y:{}".format(a, b)) 

	x += a 
	y += b 

	if x < 0 or x > 9: 
		hp -= 5 
		x -= a 
		print("You hit the wall, you loose 5 points, your HP score is {}".format(hp))

	elif y < 0 or y > 9: 
		hp -= 5 
		y -= b 
		print("You hit the wall, you loose 5 points, your HP score is {}".format(hp))
		print("Your position is X:{},Y:{}".format(x, y))
	else: 
		print("Your move was successful, your current position is X:{},Y:{} and HP:{}".format(x, y, hp))

	return x, y, hp


print(move((1, 1, 10), (-1, 0))) #=> (0, 1, 10)
print(move((0, 1, 10), (-1, 0))) #=> (0, 1, 5)
print(move((0, 1, 10), (0, 5))) #=> (0, 6, 10)
print(move((0, 9, 5), (0, 1))) #=> (0, 9, 0)