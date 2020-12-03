import pygame
import time
from settings import *

#Initialize Game
pygame.init()
screen = pygame.display.set_mode((size))
pygame.display.set_caption(TITLE)

# Player Class
class Dino(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__(dinos)  
        self.image = dinoimg
        self.rect = self.image.get_rect(topleft=pos)
        self.dino_row, self.dino_col = pos
        self.dino_x = 0
        self.dino_y = 0
        self.dino_speed = TS
        pygame.key.set_repeat(200, TS)
    
    # draw the player on the screen
    def draw(self):
        screen.blit(self.image, self.rect)

    # Lets the player move around the screen
    def move(self, dino_x, dino_y):
        if dino_x != 0:
            self.move_SA(dino_x, 0)
        if dino_y != 0:
            self.move_SA(0, dino_y)

    #Dino can't walk through walls this prevents him from proceeding if there a barrier
    def move_SA(self, dino_x, dino_y):
        self.rect.x += dino_x * TS
        self.rect.y += dino_y * TS
        for bound in bounds:
            if self.rect.colliderect(bound.rect):
                # print('Hit a wall!')
                if dino_x > 0:
                    self.rect.right = bound.rect.left
                if dino_x < 0:
                    self.rect.left = bound.rect.right
                if dino_y > 0:
                    self.rect.bottom = bound.rect.top
                if dino_y < 0:
                    self.rect.top = bound.rect.bottom

#Enemy class
class Enemy(pygame.sprite.Sprite):
    def __init__(self, pos):
        # pos = 0,0
        super().__init__(enemies)
        self.image = enemy
        self.rect = self.image.get_rect(topleft=pos)
        self.enemy_row = pos[0]
        self.enemy_col = pos[1]
        self.enemy_speed = TS
        #pygame.key.set_repeat(200, TS)

    # draw the player on the screen
    def draw(self):
        screen.blit(self.image, self.rect)

    # Lets the player move around the screen
    def move(self, enemy_row, enemy_col):
        if enemy_row != 0:
            self.move_SA(enemy_row, 0)
        if enemy_col != 0:
            self.move_SA(0, enemy_col)

    #Enemy can't walk through walls this prevents him from proceeding if there a barrier
    def move_SA(self, enemy_row, enemy_col):
        self.rect.x += enemy_row * TS
        self.rect.y += enemy_col * TS
        for bound in bounds:
            if self.rect.colliderect(bound.rect):
                # print('Hit a wall!')
                if enemy_row > 0:
                    self.rect.right = bound.rect.left
                if enemy_row < 0:
                    self.rect.left = bound.rect.right
                if enemy_col > 0:
                    self.rect.bottom = bound.rect.top
                if enemy_col < 0:
                    self.rect.top = bound.rect.bottom
# Mushroom Class 
class Mushroom(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__(mushrooms)
        self.image = mush1
        self.rect = self.image.get_rect(topleft=pos)
        
    # draw the mushrooms on the screen
    def draw(self):
        screen.blit(self.image, self.rect)
class Wall():
    # Wall thickness
    def __init__(self, pos):
        bounds.append(self)
        self.rect = pygame.Rect(pos[0], pos[1], TS, TS)

# creates the player
player = Dino((TS, TS))
dinos.add(player)
playerPC = Enemy((WIDTH-(TS*2), TS))
enemies.add(playerPC)

# creates the maze
# Parse the maze. B = wall, F = exit, M = mushrooms
x = y = 0
for row in maze:
    for col in row:
        if col == "B":
            Wall((x, y))
        if col == "F":
            # final_mushroom = Mushroom((x, y))
            final_mushroom = pygame.Rect(x, y, TS, TS)
        if col == "M":
            mushroom1 = Mushroom((x, y))
            mushroom1 = pygame.Rect(x, y, TS, TS)            
        x += TS
    y += TS
    x = 0

# function to show the score during the game and at the end
def showScore(first=1):
    Score = pygame.font.SysFont('roboto', 50)
    Ssurf = Score.render("SCORE P1: {0}".format(SCORE), True, green)
    Score_rect = Ssurf.get_rect()

    Score2 = pygame.font.SysFont('roboto', 75)
    Ssurf2 = Score2.render("SCORE P1: {0}".format(SCORE), True, blue)
    Score_rect2 = Ssurf2.get_rect()
    if first == 1:
        Score_rect.topleft = (0, 0)
        screen.blit(Ssurf, Score_rect)
    else:
        Score_rect2.center = (WIDTH//2, HEIGHT//2+TS*4)
        screen.blit(Ssurf2, Score_rect2)


def showScoreP2(first=1):
    Score = pygame.font.SysFont('roboto', 50)
    Ssurf = Score.render("SCORE P2: {0}".format(SCOREP2), True, white)
    Score_rect = Ssurf.get_rect()

    Score2 = pygame.font.SysFont('roboto', 75)
    Ssurf2 = Score2.render("SCORE P2: {0}".format(SCOREP2), True, green)
    Score_rect2 = Ssurf2.get_rect()
    if first == 1:
        Score_rect.bottomleft = (0, HEIGHT)
        screen.blit(Ssurf, Score_rect)
    else:
        Score_rect2.center = (WIDTH//2, HEIGHT//2+TS*4)
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
    pygame.quit()

# function to show the winner screen and score
def winner():
    screen.fill(black)
    gamewin.play()
    screen.blit(winnerp, winnerp_rect)
    showScore(0)
    pygame.display.flip()
    time.sleep(5)
    pygame.quit()

# function to show the Instruction page 2 of 3
def instruct():
    global instruct
    while instruct:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    button.play()
                    instruct = False
                    break
                    gameloop()
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
        screen.blit(instructions, instructions_rect)       
        screen.blit(rules, rules_rect)       
        screen.blit(enterkey, enterkey_rect)        
        screen.blit(startenter, startenter_rect)        
        screen.blit(move, move_rect)        
        screen.blit(arrows, arrows_rect)       
        screen.blit(wasd, wasd_rect)
        pygame.display.flip()

# function to show the title page 1 of 3
def game_intro():
    global intro
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    button.play()
                    intro = False
                    break
                    instuctions()
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
def gameloop():
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
            pygame.draw.rect(screen, (black), final_mushroom, 1)
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
        milliseconds += clock.tick_busy_loop(40)
        # player loses if timer reaches 0
        if minutes == 0 and seconds == 0:
            gameOver()
        pygame.display.flip()

        if 1 == 1:
            der = random.randint(0, 3)
            # print(der, playerPC.enemy_row, playerPC.enemy_col, len(maze)-2, len(maze[playerPC.enemy_col])-2)
            # print(der, playerPC.enemy_row, playerPC.enemy_col)

            if der == 0 and playerPC.enemy_row > 1:
                # walk.play()
                playerPC.move(-1, 0)
            if der == 1 and playerPC.enemy_col < len(maze) - 1:
                # walk.play()
                playerPC.move(0, 1)

            # if der == 2 and playerPC.enemy_row < len(maze[playerPC.enemy_col]) - 2:
            if der == 2 and playerPC.enemy_row < len(maze) - 2:
                # walk.play()
                playerPC.move(1, 0)

            if der == 3 and playerPC.enemy_col > 1:
                # walk.play()
                playerPC.move(0, -1)

            
        for event in pygame.event.get():            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    # walk.play()
                    player.move(1, 0)

                if event.key == pygame.K_LEFT:
                    # walk.play()
                    player.move(-1, 0)

                if event.key == pygame.K_RIGHT:
                    # walk.play()
                    player.move(1, 0)

                if event.key == pygame.K_UP:
                    # walk.play()
                    player.move(0, -1)

                if event.key == pygame.K_DOWN:
                    # walk.play()
                    player.move(0, 1)

                

                if event.key == pygame.K_ESCAPE:
                    pygame.event.post(pygame.event.Event(pygame.quit()))    

            # When Dino reaches the exit they win if collected at least 5 mushrooms, lose if not.         
            global SCORE, SCOREP2
            if player.rect.colliderect(final_mushroom) and SCORE >= 5:
                winner()
                
            if player.rect.colliderect(final_mushroom) and SCORE < 5:
                gameOver()  
        
            # Will remove/clear mushrooms from the board. Collect and increase score
            if pygame.sprite.groupcollide(dinos, mushrooms, False, True):
                collect.play()
                print("MUSHROOM COLLECTED!")
                SCORE += 1
            if pygame.sprite.groupcollide(enemies, mushrooms, False, True):
                collect.play()
                print("MUSHROOM COLLECTED!")
                SCOREP2 += 1
 
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
game_intro()
instruct()
gameloop()
pygame.quit()
