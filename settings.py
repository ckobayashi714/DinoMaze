import random
import pygame

# Sprite Groups
dinos = pygame.sprite.Group()
enemies = pygame.sprite.Group()
mushrooms = pygame.sprite.Group()


# Global Variables 
size = WIDTH, HEIGHT = 1056, 800
TS = 32
dino_size = D_WIDTH, D_HEIGHT = TS, TS
TITLE = 'DINO MAZE'
SCORE = 0
SCOREP2 = 0
bounds = []
minutes = 5
seconds = 0
milliseconds = 0

# Colors
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 225, 225)
red = pygame.Color(255, 0, 0)
yellow = pygame.Color(255, 255, 0)
blue = pygame.Color(0, 0, 255)
green = pygame.Color(0, 255, 0)
purple = pygame.Color(143, 0, 255)


# For the while loops
instruct = True
credit = True
intro = True

########################################### Background Images
background = pygame.image.load('sprites/background/backg.png')
background = pygame.transform.scale(background, (WIDTH, HEIGHT))
background_rect = background.get_rect(topleft=(0,0))

########################################### Game Music
pygame.mixer.init()
pygame.mixer.music.load('music_and_sounds/intro.wav')
pygame.mixer.music.set_volume(0)
#0.5
pygame.mixer.music.play(0)
#-1

########################################### Game Sound FX
collect = pygame.mixer.Sound('music_and_sounds/collect.wav')
collect.set_volume(0)
#0.2 all

button = pygame.mixer.Sound('music_and_sounds/button.wav')
button.set_volume(0)

walk = pygame.mixer.Sound('music_and_sounds/jump.wav')
walk.set_volume(0)
#0.05

gamewin = pygame.mixer.Sound('music_and_sounds/gamewin.wav')
gamewin.set_volume(0)

gameover = pygame.mixer.Sound('music_and_sounds/gameover.wav')
gameover.set_volume(0)

########################################### Dino player Sprite
dinoimg = pygame.image.load('sprites/dino/dino.png')
dinoimg = pygame.transform.scale(dinoimg, (dino_size))

########################################### Mushroom Sprite
mush1 = pygame.image.load('sprites/dino/mushroom1.png')
mush1 = pygame.transform.scale(mush1, (dino_size))

########################################### Computer Player Sprite
enemy = pygame.image.load('sprites/dino/enemy.png')
enemy = pygame.transform.scale(enemy, (dino_size))

###########################################  GameOver function
lost = pygame.image.load('sprites/GO.png')
lost_rect = lost.get_rect(center=(WIDTH//2, HEIGHT//2))

###########################################  Winner function
winnerp = pygame.image.load('sprites/winner.png')
winnerp_rect = winnerp.get_rect(center=(WIDTH//2, HEIGHT//2))

###########################################  Game Intro Page Images
menutitle = pygame.image.load('sprites/dinomaze.png')
menutitle_rect = menutitle.get_rect(midtop=(WIDTH//2, TS*6))
# menutitle = pygame.transform.scale(menutitle, (WIDTH, HEIGHT))

pressSB = pygame.image.load('sprites/pressSB.png')
pressSB_rect = pressSB.get_rect(center=(WIDTH//2, TS*15))

########################################## Instruction Page Images 
instructions = pygame.image.load('sprites/gameinst.png')
instructions_rect = instructions.get_rect(midtop=(WIDTH//2, 0))

rules = pygame.image.load('sprites/keys/help.png')
rules_rect = rules.get_rect(midtop=(WIDTH//2, TS*4))

move = pygame.image.load('sprites/keys/move.png')
move_rect = move.get_rect(center=(WIDTH//2, HEIGHT//2))

arrows = pygame.image.load('sprites/keys/arrows.png')
arrows = pygame.transform.scale(arrows, (225, 150))
arrows_rect = arrows.get_rect(midright=(WIDTH//2, HEIGHT//2+TS*3))

wasd = pygame.image.load('sprites/keys/wasd.png')
wasd = pygame.transform.scale(wasd, (225, 150))
wasd_rect = wasd.get_rect(midleft=(WIDTH//2, HEIGHT//2+TS*3))

enterkey = pygame.image.load('sprites/keys/enter.png')
enterkey = pygame.transform.scale(enterkey, (250, 200))
enterkey_rect = enterkey.get_rect(topleft=(WIDTH//2+TS*4, TS*16))

startenter = pygame.image.load('sprites/keys/enterStart.png')
startenter_rect = startenter.get_rect(topleft=(TS*2, TS*19))

########################################## Maze for player to beat
# Depth-First-Search Maze Algorithm
# Creates Random mazes 
# Creates a board filled all B's
def generateFilledMaze(rows, cols):
    maze = []
    for row in range(0, rows):
        next_row = []
        for col in range(0, cols):
            next_row.append("B")
        maze.append(next_row)
    return maze

# Random spot is chosen on the board recursion is used to create the maze
def createMaze(maze):    
    start_row = (random.randint(0, (len(maze) - 3)//2)) * 2 + 1
    start_col = (random.randint(0, (len(maze[start_row]) - 3)//2)) * 2 + 1
    maze[start_row][start_col] = " "
    createMazeHelper(maze, start_row, start_col)

    for row in range(1, len(maze) -1):
        for col in range(1, len(maze[row])-1):
            if maze[row][col] == " ":
                walls = 0
                if maze[row +1][col] == 'B':
                    walls += 1
                if maze[row -1][col] == 'B':
                    walls += 1
                if maze[row][col +1] == 'B':
                    walls += 1
                if maze[row][col-1]  == 'B':
                    walls += 1
                if walls == 3:  # this will add Mushrooms to maze
                    maze[row][col] = 'M' 


#Helper function recursion
def createMazeHelper(maze, r, c):
    # 0 is North, 1 is East, 2 is South, 3 is West
    dirs = [0, 1, 2, 3]
    random.shuffle(dirs)
    for dir in dirs:
        next_r = r
        next_c = c
        if dir == 0:
            next_r -= 2
        if dir == 1:
            next_c += 2
        if dir == 2:
            next_r += 2
        if dir == 3:
            next_c -= 2

        if next_r > 0 and next_r < len(maze) - 1 and next_c > 0 and next_c < len(maze[next_r]):
            if maze[next_r][next_c] == 'B':
                maze[next_r][next_c] = " "
                maze[(r+next_r)//2][(c+next_c)//2] = " "
                createMazeHelper(maze, next_r, next_c)

def printMaze(maze):
    for row in range(0, len(maze)):
        print(maze[row])

#function that randomizes maze exit location
def finalizeMaze(source_maze):
    # rad = random.randint(0, (len(source_maze)- 2) # row between 0 -> 23
    # print("random row", rad)
    # print("len of cols = ", len(source_maze[rad])-1)
    # print(source_maze[rad][len(source_maze[rad])-2])
    # if source_maze[rad][len(source_maze[rad])-2] == "B" or source_maze[rad][len(source_maze[rad])-2] == "M":
        # if source_maze[1][len(source_maze[1])-2] == "B" or source_maze[1][len(source_maze[1])-2] == "M":
            # finalizeMaze(source_maze)
        # else:
    if source_maze[1][len(source_maze[1]) - 2] == "M":
        # print("is maze here", source_maze[1][len(source_maze[1]) - 2])
        source_maze[1][len(source_maze[1]) - 2] = " "
    source_maze[1][len(source_maze[1]) - 1] = "F"
    
        
    # else:
    #     source_maze[rad][len(source_maze[rad])-1] = "F"

    final_maze = []
    for row in range(0, len(source_maze)):
        next_row = ''
        for col in range(0, len(source_maze[row])):
            next_row += source_maze[row][col]
        final_maze.append(next_row)
    return final_maze

#function for Enemy to find the closest Mushroom using Breath First Search BFS
def findMushroom(row, col, maze):
    visited = [[0] * len(maze[0]) for i in range(len(maze))]
    options = []
    initial = (row, col, '')
    options.append(initial)
    while(len(options) > 0):
        op = options[0]
        visited[op[0]][op[1]] = 1
        options = options[1:]
        if maze[op[0]][op[1]] == "B" or maze[op[0]][op[1]] == "F":
            pass #Do nothing if there is a Wall or Final Mushroom
        elif maze[op[0]][op[1]] == "M":
            # print("row, col, path", op)
            return op[2]
        else:
            north = (op[0] - 1, op[1], op[2] + "0")

            # print(visited)
            # print(north)
            if visited[north[0]][north[1]] == 0:
                options.append(north)

            east = (op[0], op[1] + 1, op[2] + "1")
            if visited[east[0]][east[1]] == 0:
                options.append(east)

            south = (op[0] + 1, op[1], op[2] + "2")
            if visited[south[0]][south[1]] == 0:
                options.append(south)

            west = (op[0], op[1] - 1, op[2] + "3")
            if visited[west[0]][west[1]] == 0:
                options.append(west)
    # print(options)
    print("no mushrooms found")
    return("Fail: No Mushrooms Found")

#creating the random maze
maze = generateFilledMaze(25, 33)
createMaze(maze)
maze = finalizeMaze(maze)
# printMaze(maze)

"""maze = [
    "BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB",
    "B  BBB BB BBBM   B   B         B",
    "B    B    BBBBB BB B B BBBBBBB B",
    "BBBB B B  B   B BB B B   B M B B",
    "B      B    B B  B B B B   B   B",
    "B B BB B  BBBBBB   B B BBBBBBB B",
    "B B  B BB    B BBBBB B         B",
    "BBB  BBBBBBB B       B   BBB   B",
    "B BB     B     BB  BBB  BBBBB  B",
    "B    BB BB  BBBBB       B  MB  B",
    "B   BB   BB    BB BBBB BBABBBBBB",
    "B  BB     BB   B  B  B BB B  B B",
    "BMBB  B B  BB  B  B  B    BB B B",
    "BBB         BB B     B BB  B  MB",
    "BB  B  B  B  B B  B  B BB  B BBB",
    "BBB         BB B BB  BBBBBBB   B",
    "B BBB BBBBBBB  B B  BB         B",
    "B   B     B    B B  B     BBBBBB",
    "B B B     B BB B BB BBBABBB    B",
    "B B B     B BB B  B       B BB B",
    "B B BB   BB BB B  B    BB B MB B",
    "B B  B BBB  BB B  BBB BB  BBBB B",
    "BMBB   BM   BB         B       F",
    "BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB"
]"""
########################################### Unused labels
#old size HEIGHT, WIDTH = 1024, 768

##### Game Over
# GO = 'GAMEOVER'
# GO = pygame.font.SysFont('impact', 100)
# GOsurf = GO.render(GO, True, red)
# GO_rect = GOsurf.get_rect(midbottom=(WIDTH//2, HEIGHT//2))
# screen.blit(GOsurf, GO_rect)

##### Winner
# WIN = 'YOU WIN!'
# Win = pygame.font.SysFont('impact', 100)
# Wsurf = Win.render(WIN, True, green)
# Win_rect = Wsurf.get_rect(midbottom=(WIDTH//2, HEIGHT//2))
# screen.blit(Wsurf, Win_rect)

#### Instruction Page
# START = 'DINO MAZE'
# Start = pygame.font.SysFont('impact', 120)
# Ssurf = Start.render(START, True, blue)
# Srect_rect = Ssurf.get_rect(center = (WIDTH//2, HEIGHT//2))
# screen.blit(Ssurf, Srect_rect)

# SPACE = 'PRESS SPACEBAR TO CONTINUE'
# Start = pygame.font.SysFont('impact', 40)
# Ssurf = Start.render(SPACE, True, blue)
# Srect_rect = Ssurf.get_rect(center = (WIDTH//2, HEIGHT//2+192))
# screen.blit(Ssurf, Srect_rect)

########################################### Unused Functions
# To help draw on screen
screen = pygame.display.set_mode((size))
TILESIZE = 32
GRIDWIDTH = WIDTH / TILESIZE
GRIDHEIGHT = HEIGHT / TILESIZE
lightgrey = pygame.Color(100, 100, 100)
darkgrey = pygame.Color(40, 40, 40)
def draw_grid():
    for x in range(0, WIDTH, TILESIZE):
        pygame.draw.line(screen, lightgrey, (x, 0), (x, HEIGHT))
    for y in range(0, HEIGHT, TILESIZE):
        pygame.draw.line(screen, lightgrey, (0, y), (WIDTH, y))

########################################### Trying to make an easter egg (unsuccessful)
# def credits(credit):
#     while credit:
#         for event in pygame.event.get():
#             if event.type == pygame.KEYDOWN:
#                 if event.key == pygame.K_ESCAPE:
#                     credit = False
#                     pygame.quit()
#             if event.type == pygame.QUIT:
#                 credit = False
#                 pygame.quit()

#     screen.fill(black)
#     cassandra = pygame.image.load('sprites/cassandra.png')
#     cassandra_rect = cassandra.get_rect(center=(WIDTH//2, HEIGHT//2))
#     screen.blit(cassandra, cassandra_rect)
#     pygame.display.flip()
#     time.sleep(5)
#     pygame.quit()
