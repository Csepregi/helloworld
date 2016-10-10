hallway = [0] * 100
step = 1

while step <= len(hallway):
    door = step - 1
    while door < len(hallway):
        if hallway[door] == 0:
            hallway[door] = 1
        else:
            hallway[door] = 0
        door = door + step
    step = step +1

for door in range(0, len(hallway)):
    if hallway[door] == 1:
        print("Open: ", door+1)

