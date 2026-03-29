
def crew():
	change_hat(Hats.Traffic_Cone)
	while True :
		for i in range(get_world_size()):
			if can_harvest():
				harvest()
				move(North)
			else:
				move(North)
		move(East)

for i in range(max_drones()):
	spawn_drone(crew)
	move(East)
move(West)
while True :
	for i in range(get_world_size()):
		if can_harvest():
			harvest()
			move(North)
		else:
			move(North)
	move(East)
