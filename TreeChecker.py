clear()
while True:
    if can_harvest():
        harvest()
    x = get_pos_x() 
    y = get_pos_y() 
    if (x % 2 == 0 and y % 2 == 0) or (x % 2 == 1 and y % 2 == 1):

        plant(Entities.Tree)
    else:
        plant(Entities.Bush)

    move(East)

    if x == get_world_size() - 1:
        move(North)
