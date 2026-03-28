#Not the greatest code there is cuz most of code feature still locked
while True :
	for i in range(2):
		for i in range(get_world_size()) :
			if(can_harvest()) :
				harvest()
			move(North)
		move(East)
	
	for i in range(2):
		for i in range(get_world_size()):
			if(can_harvest()):
				harvest()
				plant(Entities.Tree)
        #change this into bush
			else:
				use_item(Items.Water)
        #delete this if still cant use water
			move(North)
		move(East)

  #till 2x6 soil on (5,6) to (6,0)before run this code
	for i in range(2):
		for i in range(get_world_size()):
			if (Entities.Carrot):
				harvest()
				plant(Entities.Carrot)
			move(North)
		move(East)
		
		
			
