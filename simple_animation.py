import sys, pygame
import time
import random
pygame.init()
white=(255,255,255)
size = width, height = 800, 600
speed = [20,0]
black = 0, 0, 0
car_width =128
screen = pygame.display.set_mode(size)
pygame.display.set_caption("my game")
clock=pygame.time.Clock()
ballimg = pygame.image.load("ball.png")
ballrect = ballimg.get_rect()
print ballrect
def car(x,y):
    #screen.blit(ballimg,ballrect)
    screen.blit(ballimg,(x,y))

def text_objects(text,font):
    textSurface=font.render(text,True,black)
    return textSurface,textSurface.get_rect()
  
def obstacles(thingx,thingy,thingw,thingh,color):
    pygame.draw.rect(screen,color,[thingx,thingy,thingw,thingh])
 
def display_message(text):
    textfont=pygame.font.Font('freesansbold.ttf',115)
    TextSurf,TextRect=text_objects(text,textfont)
    TextRect.center=((width/2),(height/2))
    screen.blit(TextSurf,TextRect)
    pygame.display.update() 
    time.sleep(2)
    game_loop()

def crash():
    display_message("You crashed!")


def game_loop() :
    car_xdist=width * 0.45
    car_ydist=height *0.8
    thing_x=random.randrange(0,width)
    thing_y=-400
    thing_w =100
    thing_h =100
    thing_speed =7

    x_change =0
    #crashed=False
    game_exit=False
    while not game_exit:
        for event in pygame.event.get():
           if event.type==pygame.QUIT:
              game_exit=True
              sys.exit()
           
           if event.type == pygame.KEYDOWN:
              if event.key == pygame.K_LEFT:
                 x_change =-5
              if event.key == pygame.K_RIGHT:
                 x_change =5
           
           if event.type == pygame.KEYUP:
              x_change =0
        car_xdist+= x_change
           #print(event)
        screen.fill(white)
        obstacles(thing_x,thing_y,thing_w,thing_h,black)
        thing_y+= thing_speed

        car(car_xdist,car_ydist)
        if thing_y > height:
           thing_y= 0 - thing_h
           thing_x=random.randrange(0,width)
        if car_xdist > (width - car_width)or car_xdist <0:
           crash()
        if car_ydist< thing_y +thing_h:
            print "y crossover"
            if car_xdist > thing_x and car_xdist < thing_x + thing_w or car_xdist +car_width > thing_x and car_xdist + car_width < thing_x +thing_w:
                print "x crossover"
                crash()
        pygame.display.update() #if no parameter mentioned in paranthesis then it displays entire surface other wise it will update that specific paramater
        clock.tick(60)

game_loop()

