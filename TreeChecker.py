
while True:
    if can_harvest():
        harvest()

    # Get current coordinates
    x = get_pos_x()  # Current column (0, 1, 2, etc.)
    y = get_pos_y()  # Current row (0, 1, 2, etc.)

    # Checkerboard logic: Plant trees on "black squares", bushes on "white squares"
    # This ensures no two trees are adjacent (since trees need space to grow lol)
    if (x % 2 == 0 and y % 2 == 0) or (x % 2 == 1 and y % 2 == 1):
        # "Black squares" - plant trees
        plant(Entities.Tree)
    else:
        # "White squares" - plant bushes
        plant(Entities.Bush)

    move(East)

    if x == get_world_size() - 1:
        move(North)
