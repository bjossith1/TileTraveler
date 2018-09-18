# Player starts at 1,1 and can only move north
# We tell the player what directions he can move to
# If he enters a direction which is not available we print not a valid direction and let him try again
# PLayer wins when he gets to the tile 3,1 and we print out Victory!

#Directions the player can move to in each tile:
# 1,1 -> N
# 1,2 -> N,E,S
# 1,3 -> E,S
# 2,1 -> N
# 2,2 -> W, S
# 2,3 -> E, W
# 3,1 -> Victory!
# 3,2 -> N,S
# 3,3 -> W,S

north = ("n" or "N")
east = ("e" or "E")
west = ("w" or "W")
south = ("s" or "S")


valid_direction = ""

if x == 1 and y == 1:
    print("You can travel: (N)orth")
    valid_direction == north

if x == 1 and y == 2:
    print("You can travel: (N)orth or (E)ast or (S)outh")
    valid_direction == north or east or south

if x == 1 and y == 3:
    print("You can travel: (E)ast or (S)outh")
    valid_direction == east or south

if x == 2 and y == 1:
    print("You can travel: (N)orth")
    valid_direction == north

if x == 2 and y == 2:
    print("You can travel: (S)outh or (W)est")
    valid_direction == south or west

if x == 2 and y == 3:
    print("You can travel: (W)est or (E)ast")
    valid_direction == west or east

if x == 3 and y == 1:
    print ("Victory!")

if x == 3 and y == 2:
    print("You can travel: (N)orth or (S)outh")
    valid_direction == north or south

if x == 3 and y == 3:
    print("You can travel: (W)est or (S)outh")
    valid_direction == west or south

x = 1
y = 1
d = input("Direction: ")

while d == valid_direction:



