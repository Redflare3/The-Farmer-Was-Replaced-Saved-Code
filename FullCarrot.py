clear()
while True :
	for i in range(get_world_size()) :
		if(get_ground_type()==Grounds.Grassland):
			till()
			move(North)
		else:
			harvest()
			plant(Entities.Carrot)
			move(North)
	move(East)
#just straight foward no need explaination
