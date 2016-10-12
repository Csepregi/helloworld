tab = [[2,0,2,2],[2,2,2,2],[0,0,2,0],[2,0,2,0]]
print("_"*32)
for i in range(4):
   print("| %4d  | %4d  | %4d  | %4d  |" % (tab[i][0],tab[i][1],tab[i][2],tab[i][3]))
   print("_"*32)
   print()
import random
def tab_start():
   tab = []
   global tab
   for i in range(4):
       tab.append([0,0,0,0])
   rand = []
   for r in range(4):
       rand.append(random.randrange(0,3))
   tab[rand[0]][rand[1]] = 2
   tab[rand[2]][rand[3]] = 2
   print("_"*32)
   for i in range(4):
       print("| %4d  | %4d  | %4d  | %4d  |" % (tab[i][0],tab[i][1],tab[i][2],tab[i][3]))
       print("_"*32)
       print()
   return tab
       
#def random_game():
   #random_index = []
   #for x in range(4):
       #for y in range(4):
           #if tab[x][y] == 0:
               #random_index.append([x,y])
    #a = random.choice(random_index)
    #r1 = a[0]
    #r2 = a[1]
    #tab[r1][r2] = 2    
    
def move_horizontal(a,b):
    
   for x in range(4):
       for rep in range(3):
           for y in range(3):
               if tab[x][y+a] == 0 and tab[x][y+b] != 0:
                   tab[x][y+a] = tab[x][y+b]
                   tab[x][y+b] = 0

def move_vertical(up,down):

   for y in range(4):
       for rep in range(3):
           for x in range(3):
               if tab[x+up][y] == 0 and tab[x+down][y] != 0:
                   tab[x+up][y] = tab[x+down][y]
                   tab[x+down][y] = 0
def add_left():

   for x in range(4):
       for rep in range(3):
           for y in range(3):
               if tab[x][y] == tab[x][y+1]:
                   tab[x][y+1] *= 2
                   tab[x][y] = 0
def add_right():

   for x in range(4):
       for rep in range(3):
           for y in reversed(range(3)):
               if tab[x][y] == tab[x][y+1]:
                   tab[x][y+1] *= 2
                   tab[x][y] = 0

def add_up():

   for y in range(4):
       for rep in range(3):
           for x in range(3):
               if tab[x+1][y] == tab[x][y]:
                   tab[x][y] *= 2
                   tab[x+1][y] = 0

def add_down():

  for y in range(4):
       for rep in range(3):
           for x in reversed(range(3)):
               if tab[x+1][y] == tab[x][y]:
                   tab[x][y] *= 2
                   tab[x+1][y] = 0


tab_start()
move = input()

if move == "a":
   move_horizontal("up",0,1)
   add_left()
   move_horizontal(0,1)

elif move == "d":
   move_horizontal(1,0)
   add_right()
   move_horizontal(1,0)

elif move == "w":
   move_vertical(0,1)
   add_up()
   move_vertical(0,1)

elif move == "s":
   move_vertical(1,0)
   add_down()
   move_vertical(1,0)

print()
print()
print("_"*32)
for i in range(4):
   print("| %4d  | %4d  | %4d  | %4d  |" % (tab[i][0],tab[i][1],tab[i][2],tab[i][3]))
   print("_"*32)
   print()