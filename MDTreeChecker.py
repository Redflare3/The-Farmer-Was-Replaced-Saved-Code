clear()
def extra():
	change_hat(Hats.Sunflower_Hat)
	while True:
		if can_harvest():
			harvest()
		x = get_pos_x() 
		y = get_pos_y() 
		if (x % 2 == 0 and y % 2 == 0) or (x % 2 == 1 and y % 2 == 1):
	
			plant(Entities.Tree)
			use_item(Items.Weird_Substance)
			use_item(Items.Water)
		else:
			harvest()
	
		move(East)
	

for i in range(max_drones()):
		spawn_drone(extra)
		move(North)
		
move(South)
change_hat(Hats.Gold_Hat)
while True:
	if can_harvest():
		harvest()
	x = get_pos_x() 
	y = get_pos_y() 
	
	if (x % 2 == 0 and y % 2 == 0) or (x % 2 == 1 and y % 2 == 1):

		plant(Entities.Tree)
		use_item(Items.Weird_Substance)
		use_item(Items.Water)
	else:
		harvest()

	move(East)
	
	

		
