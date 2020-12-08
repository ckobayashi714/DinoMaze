import pygame
import time
from settings import *

#Initialize Game
pygame.init()
screen = pygame.display.set_mode((size))
pygame.display.set_caption(TITLE)

def clearSprites():
    dinos.clear(screen, background)
    mushrooms.clear(screen, background)
    enemies.clear(screen, background)
    walls.clear(screen, background)
    pygame.display.flip()

# Player Class
class Dino(pygame.sprite.Sprite):
    def __init__(self, pos, maze):
        super().__init__(dinos)
        self.maze = maze 
        self.image = dinoimg
        self.rect = self.image.get_rect(topleft=pos)
        self.row = 1
        self.col = 1
        self.dino_speed = TS
        pygame.key.set_repeat(200, TS)
    
    # draw the player on the screen
    def draw(self):
        screen.blit(self.image, self.rect)

    # Lets the player move around the screen
    def move(self, dino_row, dino_col):
        # print(row, col)
        if dino_row != 0:
            self.move_SA(dino_row, 0)
        if dino_col != 0:
            self.move_SA(0, dino_col)

    #Dino can't walk through walls this prevents him from proceeding if there a barrier
    def move_SA(self, dino_row, dino_col):
            self.row += dino_row
            self.col += dino_col
            # print(self.row, self.col)
            if self.maze[self.row][self.col] == 'B':
                # print(self.row, self.col)
                self.row -= dino_row
                self.col -= dino_col
            self.rect.x = self.col * TS
            self.rect.y = self.row * TS

#Enemy class
class Enemy(pygame.sprite.Sprite):
    def __init__(self, pos, maze):
        super().__init__(enemies)
        self.maze = maze
        self.image = enemy
        self.rect = self.image.get_rect(topleft=pos)
        self.row = 1
        self.col = len(maze[self.row]) - 2
        self.move_counter = 0
        self.move_SA(0, 0)       
        self.enemy_speed = TS
        pygame.key.set_repeat(200, TS)

    # draw the player on the screen
    def draw(self):
        screen.blit(self.image, self.rect)

    # Lets the player move around the screen
    def move(self, enemy_row, enemy_col):
        if enemy_row != 0:
            self.move_SA(enemy_row, 0)
        if enemy_col != 0:
            self.move_SA(0, enemy_col)

    #Enemy can't walk through walls this prevents him from proceeding if there's a barrier
    def move_SA(self, enemy_row, enemy_col):
        self.row += enemy_row
        self.col += enemy_col
        if self.maze[self.row][self.col] == 'B' or self.maze[self.row][self.col] == 'F':
            self.row -= enemy_row
            self.col -= enemy_col
        else:
            self.move_counter = 0
        self.rect.x = self.col * TS
        self.rect.y = self.row * TS

# Mushroom Class 
class Mushroom(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__(mushrooms)
        self.image = mush1
        self.rect = self.image.get_rect(topleft=pos)
        
    # draw the mushrooms on the screen
    def draw(self):
        screen.blit(self.image, self.rect)


class Wall(pygame.sprite.Sprite):
    # Wall thickness
    def __init__(self, pos):
        super().__init__(walls)
        bounds.append(self)
        self.rect = pygame.Rect(pos[0], pos[1], TS, TS)

    # def draw(self):
    #     screen.blit(self.image, self.rect)
        


# function to show the score during the game and at the end
def showScore(first=1):
    Score = pygame.font.SysFont('roboto', 50)
    Ssurf = Score.render("P1 SCORE: {0}".format(SCORE), True, green)
    Score_rect = Ssurf.get_rect()

    Score2 = pygame.font.SysFont('roboto', 75)
    Ssurf2 = Score2.render("P1 SCORE: {0}".format(SCORE), True, blue)
    Score_rect2 = Ssurf2.get_rect()
    if first == 1:
        Score_rect.topleft = (0, 0)
        screen.blit(Ssurf, Score_rect)
    else:
        Score_rect2.center = (WIDTH//2, HEIGHT//2+TS*4)
        screen.blit(Ssurf2, Score_rect2)


def showScoreP2(first=1):
    Score = pygame.font.SysFont('roboto', 50)
    Ssurf = Score.render("P2 SCORE: {0}".format(SCOREP2), True, yellow)
    Score_rect = Ssurf.get_rect()

    Score2 = pygame.font.SysFont('roboto', 75)
    Ssurf2 = Score2.render("P2 SCORE: {0}".format(SCOREP2), True, green)
    Score_rect2 = Ssurf2.get_rect()
    if first == 1:
        Score_rect.bottomleft = (0, 25*TS+3)
        screen.blit(Ssurf, Score_rect)
    else:
        Score_rect2.leftbottom = (WIDTH//2, HEIGHT//2+TS*4)
        screen.blit(Ssurf2, Score_rect2)

# function to show the countdown timer during the game
def timer():
    Timer = pygame.font.SysFont('roboto', 50)
    Tsurf = Timer.render("TIMER {}:{}".format(minutes, seconds), True, red)
    Timer_rect = Tsurf.get_rect(topleft=(TS*27, 0))
    screen.blit(Tsurf, Timer_rect)

# function to show the gameover screen and score
def gameOver():
    screen.fill(black)
    gameover.play()
    screen.blit(lost, lost_rect)
    showScore(0)
    pygame.display.flip()
    time.sleep(5)


# function to show the winner screen and score
def winner():
    screen.fill(black)
    gamewin.play()
    screen.blit(winnerp, winnerp_rect)
    showScore(0)
    pygame.display.flip()
    time.sleep(5)


# function to show the Instruction page 2 of 3
def instructions():
    global ran
    instruct = True
    while instruct:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == ord('e'):
                    ran = 50
                    button.play()
                    instruct = False
                    break
                    gameloop(ran)

                if event.key == ord('m'):
                    ran = 25
                    button.play()
                    instruct = False
                    break
                    gameloop(ran)

                if event.key == ord('h'):
                    ran = 1
                    button.play()
                    instruct = False
                    break
                    gameloop(ran)

                if event.key == pygame.K_RETURN:
                    ran = 1
                    button.play()
                    instruct = False
                    break
                    gameloop(ran)

                if event.key == pygame.K_ESCAPE:
                    instruct = False
                    time.sleep(1)
                    pygame.quit()

            if event.type == pygame.QUIT:
                instruct = False
                pygame.quit()

        #PNG imgs on instruction screen
        screen.fill(black)  
        screen.blit(background, background_rect)
        screen.blit(instructionspg, instructionspg_rect)       
        screen.blit(rules, rules_rect)       
        screen.blit(enterkey, enterkey_rect)        
        screen.blit(startenter, startenter_rect)        
        screen.blit(move, move_rect)        
        screen.blit(arrows, arrows_rect)       
        screen.blit(wasd, wasd_rect)
        pygame.display.flip()

# function to show the title page 1 of 3
def game_intro():
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    button.play()
                    intro = False
                    break
                    instructions()
                if event.key == pygame.K_ESCAPE:
                    intro = False
                    time.sleep(1)
                    pygame.quit()
            if event.type == pygame.QUIT:
                intro = False
                pygame.quit()

        #PNG imgs on game intro screen
        screen.fill(black)
        screen.blit(background, background_rect)
        screen.blit(menutitle, menutitle_rect)
        screen.blit(pressSB, pressSB_rect)
        pygame.display.flip()

# function to play the game page 3 of 3
def gameloop(ran):
    # start the timer
    clock = pygame.time.Clock()
    running = True
    while running:
        # set the whole scene and board
        screen.fill(white)
        screen.blit(background, background_rect)
        # draw_grid()
        # create the maze and mushrooms on the screen   
        for bound in bounds:
            pygame.draw.rect(screen, (black), bound.rect)
            pygame.draw.rect(screen, (purple), final_mushroom)
            # pygame.draw.rect(screen, (yellow), final_mushroom, 2)
        # draw the players, mushrooms, and baddies
        dinos.draw(screen)
        mushrooms.draw(screen)
        enemies.draw(screen)
        showScore()
        showScoreP2()
        # update the timer
        global milliseconds, seconds, minutes
        if seconds == 0:
            minutes -= 1
            seconds = 59
        if milliseconds > 1000:
            seconds -= 1
            milliseconds -= 1000
        timer()
        milliseconds += clock.tick_busy_loop(60)
        # player loses if timer reaches 0
        if minutes == 0 and seconds == 0:
            gameOver()
            clearSprites()
            running = False
            

        pygame.display.flip()

        playerPC.move_counter += 1
        roll = random.randint(0, playerPC.move_counter)
        # print(playerPC.move_counter)

        global SCORE, SCOREP2

        if roll > ran:
            path = findMushroom(playerPC.row, playerPC.col, maze)
            # print(path)
            # printMaze(maze)
            if path == '':
                path = findPlayer(playerPC.row, playerPC.col, maze, player.row, player.col)
            der = int(path[0])
            
            # print(der, playerPC.row, playerPC.col)
            if der == 0: #down
                # walk.play()
                playerPC.move(-1, 0)

            if der == 1: #right
                # walk.play()right
                playerPC.move(0, 1)

            if der == 2 : #up
                # walk.play()
                playerPC.move(1, 0)

            if der == 3 : #left
                # walk.play()
                playerPC.move(0, -1)
            
            if maze[playerPC.row][playerPC.col] == "M":
                maze[playerPC.row] = maze[playerPC.row][0: playerPC.col] + \
                    " " + maze[playerPC.row][playerPC.col + 1: ]
                pygame.sprite.groupcollide(enemies, mushrooms, False, True)
                SCOREP2 += 1
            
            if playerPC.rect.colliderect(player.rect):
                gameOver()
                clearSprites()
                running = False
                

        for event in pygame.event.get():            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    # walk.play()
                    player.move(0, 1)

                if event.key == pygame.K_UP:
                    # walk.play()
                    player.move(-1, 0)

                if event.key == pygame.K_DOWN:
                    # walk.play()
                    player.move(1, 0)

                if event.key == pygame.K_LEFT:
                    # walk.play()
                    player.move(0, -1)

                if event.key == pygame.K_RIGHT:
                    # walk.play()
                    player.move(0, 1)

                if event.key == pygame.K_ESCAPE:
                    pygame.event.post(pygame.event.Event(pygame.quit()))    
            
            # Will remove/clear mushrooms from the board. Collect and increase score    
            if maze[player.row][player.col] == "M":
                maze[player.row] = maze[player.row][0: player.col] + \
                    " " + maze[player.row][player.col + 1:]
                pygame.sprite.groupcollide(dinos, mushrooms, False, True)
                collect.play()
                # print("MUSHROOM COLLECTED!")
                SCORE += 1

            # When Dino reaches the exit they win if collected more mushrooms than Enemy, lose if not.         
            if player.rect.colliderect(final_mushroom) and SCORE >= SCOREP2:
                winner()
                clearSprites()
                running = False
                
                
            if player.rect.colliderect(final_mushroom) and SCORE < SCOREP2:
                gameOver()
                clearSprites()
                running = False
                

            if player.rect.colliderect(playerPC.rect):
                gameOver()
                clearSprites()
                running = False
                

            
            if event.type == pygame.QUIT:
                clearSprites()
                running = False            
                pygame.quit()
                return True
    print("Now Outside of Game")
    return False


quitting = False
while quitting == False:
    # creates the player
    dinos = pygame.sprite.Group()
    enemies = pygame.sprite.Group()
    mushrooms = pygame.sprite.Group()
    walls = pygame.sprite.Group()

    maze = generateFilledMaze(25, 33)
    createMaze(maze)
    maze = finalizeMaze(maze)
    printMaze(maze)

    player = Dino((TS, TS), maze)
    dinos.add(player)
    playerPC = Enemy((TS, TS), maze)
    enemies.add(playerPC)
    ran = 50
    

    # creates the maze
    # Parse the maze. B = wall, F = exit, M = mushrooms
    x = y = 0
    for row in maze:
        for col in row:
            if col == "B":
                hello = Wall((x, y))
                hello = pygame.Rect(x, y, TS, TS)
            if col == "F":
                # final_mushroom = Mushroom((x, y))
                final_mushroom = pygame.Rect(x, y, TS, TS)
            if col == "M":
                mushroom1 = Mushroom((x, y))
                mushroom1 = pygame.Rect(x, y, TS, TS)
            x += TS
        y += TS
        x = 0
    
    game_intro()
    instructions()
    quitting = gameloop(ran)
    
pygame.quit()
