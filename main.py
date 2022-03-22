import pygame
pygame.init()  
pygame.display.set_caption("platformer")  # sets the window title
screen = pygame.display.set_mode((800, 800))  # creates game screen
screen.fill((0,0,0))
clock = pygame.time.Clock() #set up clock
gameover = False #variable to run our game loop

Mark = pygame.image.load('dude.png') #load your spritesheet
Mark.set_colorkey((255, 0, 255)) #this makes bright pink (255, 0, 255) transparent (sort of)
red = (255,0,0)
purple = (200,0,200)
Mark = pygame.transform.scale(Mark, (2, 2))

#CONSTANTS
LEFT=0
RIGHT=1
UP = 2
DOWN = 3

#platform class

class Rectangular:
    def __init__ (self, xpos, ypos):
        self.xpos = xpos
        self.ypos = ypos
    def draw(self):
        pygame.draw.rect(screen, (red),(self.xpos, self.ypos, 100, 20))
    def collide(self, x, y):
        if x>self.xpos and x<self.xpos+100 and y+40> self.ypos and y +20 < self.ypos + 20:
            return self.ypos
        else:
            return False
class Square:
    def __init__ (self, xpos, ypos):
        self.xpos = xpos
        self.ypos = ypos
    def draw(self):
        pygame.draw.rect(screen, (red),(self.xpos, self.ypos, 20, 20))
    def collide(self, x, y):
        if x>self.xpos and x<self.xpos+100 and y+40> self.ypos and y+40 < self.ypos + 20:
            return self.ypos
        else:
            return False

#player variables
Px= 600 #xpos of player
Py= 750 #ypos of player
vx = 0 #x velocity of player
vy = 0 #y velocity of player
keys = [False, False, False, False] #this list holds whether each key has been pressed
isOnGround = False #this variable stops gravity from pulling you down more when on a platform

jump = pygame.mixer.Sound('jump.wav')
music = pygame.mixer.music.load('music.wav')
pygame.mixer.music.play(-1)

#animation variables variables
frameWidth = 16
frameHeight = 16
RowNum = 0 #for left animation, this will need to change for other animations
frameNum = 0
ticker = 0

p1 = Rectangular(400, 600)
p2 = Rectangular(100, 750)
p3 = Rectangular(250, 650)
p4 = Rectangular(525, 500)
p5  = Rectangular(300, 400)
s1 = Square(450,450)
while not gameover: #GAME LOOP############################################################
    clock.tick(60) #FPS
  
    #Input Section------------------------------------------------------------
    for event in pygame.event.get(): #quit game if x is pressed in top corner
        if event.type == pygame.QUIT:
            gameover = True
      
        if event.type == pygame.KEYDOWN: #keyboard input
            if event.key == pygame.K_LEFT:
                keys[LEFT]=True
            elif event.key == pygame.K_RIGHT:
                keys[RIGHT]=True

            elif event.key == pygame.K_UP:
                keys[UP]=True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                keys[LEFT]=False
            elif event.key == pygame.K_RIGHT:
                keys[RIGHT]=False

            elif event.key == pygame.K_UP:
                keys[UP]=False
                
    
       
          
    #physics section--------------------------------------------------------------------
    
    #LEFT MOVEMENT
    if keys[LEFT]==True:
        vx=-3
        direction = LEFT
    elif keys[RIGHT]==True:
        vx=3
        direction = RIGHT
    
    #turn off velocity
    else:
        vx = 0
        
        
      #JUMPING  
    if keys[UP] == True and isOnGround == True: 
        vy = -8
        isOnGround = False
        direction = UP
        pygame.mixer.Sound.play(jump)
    
    #ANIMATION-------------------------------------------------------------------
        
    # Update Animation Information
    # Only animate when in motion
    if vx>0:
        RowNum = 0
    if vx < 0: #left animation
        RowNum = 1
        # Ticker is a spedometer. We don't want Link animating as fast as the
        # processor can process! Update Animation Frame each time ticker goes over
        ticker+=1
        if ticker%10==0: #only change frames every 10 ticks
          frameNum+=1
           #If we are over the number of frames in our sprite, reset to 0.
           #In this particular case, there are 10 frames (0 through 9)
        if frameNum>3: 
           frameNum = 0
    
    #COLLISION
        
    isOnGround = False
    if p1.collide(Px, Py) != False:
        isOnGround = True
        vy = 0
        Py = p1.collide(Px, Py) - 20 

    elif p2.collide(Px, Py) != False:
        isOnGround = True
        vy = 0
        Py = p2.collide(Px, Py)  - 20
     
    elif p3.collide(Px, Py) != False:
        isOnGround = True
        vy = 0
        Py = p3.collide(Px, Py)  - 20
        
    elif p4.collide(Px, Py) != False:
        isOnGround = True
        vy = 0
        Py = p4.collide(Px, Py)  - 20
        
    elif p5.collide(Px, Py) != False:
        isOnGround = True
        vy = 0
        Py = p5.collide(Px, Py)  - 20
    elif s1.collide(Px, Py) != False:
        isOnGround = True
        vy = 0
        Py = s1.collide(Px, Py)  -20
    print(isOnGround)
    #stop falling if on bottom of game screen
    if Py > 780:
        isOnGround = True
        vy = 0
        Py = 780
    
    #gravity
    if isOnGround == False:
        vy+=.3 #notice this grows over time, aka ACCELERATION
    

    #update player position
    Px+=vx 
    Py+=vy
    
  
    # RENDER Section--------------------------------------------------------------------------------
            
    screen.fill((0,0,0)) #wipe screen so it doesn't smear
    screen.blit(Mark, (Px,Py), (frameWidth*frameNum*2, RowNum*frameHeight*2, frameWidth, frameHeight))
    #pygame.draw.rect(screen, (purple), (Px, Py, 20, 40))
    
    
    #class platforms
    p1.draw()
    p2.draw()
    p3.draw()
    p4.draw()
    p5.draw()
    s1.draw()
    
    pygame.display.flip()#this actually puts the pixel on the screen
    
#end game loop------------------------------------------------------------------------------
pygame.quit()
