import pygame
import time
import random
pygame.init()
clock=pygame.time.Clock()
white=(255,255,255)
blue=(0,0,1)
black=(0,0,0)
red=(255,0,0)
green=(0,155,0)
display_height=600
display_length=800
small_font=pygame.font.SysFont("comicsansms",25)
medium_font=pygame.font.SysFont("comicsansms",50)
large_font=pygame.font.SysFont("comicsansms",75)
gameDisplay=pygame.display.set_mode((display_length,display_height))
pygame.display.set_caption("bhan_game")
img=pygame.image.load('F:/snakehead.bmp')
icon=pygame.image.load('F:/apple.png')
apple_img=pygame.image.load('F:/apple.png')
pygame.display.set_icon(apple_img)
def pause():
    p=True
    while p:
        #gameDisplay.fill(green)
        message_to_screen("press c for continue", red, 0, medium_font)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key==pygame.K_c:
                    p=False
def apple_gen(apple_pos):
    randapplex = round(random.randrange(0, display_length - apple_pos) / 10.0) * 10.0
    randappley = round(random.randrange(0, display_height - apple_pos) / 10.0) * 10.0
    return randapplex,randappley
def snake_print(snake_list,change_pos,direction):
    if direction=="NONE":
        heade = pygame.transform.rotate(img,0)
    elif direction=="RIGHT":
        heade=pygame.transform.rotate(img,270)
    elif direction == "LEFT":
        heade = pygame.transform.rotate(img, 90)
    elif direction == "UP":
        heade = pygame.transform.rotate(img, 0)
    elif direction == "DOWN":
        heade = pygame.transform.rotate(img, 180)

    gameDisplay.blit(heade, [snake_list[-1][0], snake_list[-1][1]])
    for pair in snake_list[:-1]:
       pygame.draw.rect(gameDisplay, green, [pair[0], pair[1], change_pos, change_pos])
def game_start_screen():
    gameDisplay.fill(white)
    flag=True
    while flag:
        message_to_screen("Welcome to snake_booster",green,-50,medium_font)
        message_to_screen("Press c to continue and q to quit", red, 0, small_font)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                  if event.key == pygame.K_c:
                      gameloop()
                  elif event.key == pygame.K_q:
                      pygame.quit()
                      quit()
            pygame.display.update()
            clock.tick(50)
def message_to_screen(msg,color,y_displace=0,size="small_font" ):
    screen_text=size.render(msg,True,color)
    text_rect=screen_text.get_rect()
    text_rect.center=display_length/2,display_height/2+y_displace
    gameDisplay.blit(screen_text,text_rect)
def gameloop():
    direction="NONE"
    score=1
    snake_list = []
    game_over = False
    gameexit = False
    c_lead_x = int(display_length / 2)
    c_lead_y = int(display_height / 2)
    c_lead_x_change = 0
    c_lead_y_change = 0
    change_pos = 20
    apple_pos=30
    randapplex,randappley=apple_gen(apple_pos)
    prev=pygame.K_c
    while not gameexit:
        while game_over==True:
            gameDisplay.fill(black)
            message_to_screen("GAME OVER", white, 0,large_font)
            message_to_screen("press c for continue q for quit",red,100,medium_font)

            pygame.display.update()
            for event in pygame.event.get():
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_q:
                        game_over=False
                        gameexit=True
                    elif event.key==pygame.K_c:
                        prev=pygame.K_c
                        score=0
                        game_over=False
                        gameloop()
        flage=0
        
        for event in pygame.event.get():
            #print(event)
            if event.type==pygame.QUIT:
                gameexit=True
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_LEFT and prev!=pygame.K_RIGHT:
                    c_lead_x_change= -change_pos
                    c_lead_y_change = 0
                    prev=pygame.K_LEFT
                    direction="LEFT"

                elif event.key==pygame.K_RIGHT and prev!=pygame.K_LEFT:
                     c_lead_x_change= change_pos
                     c_lead_y_change=0
                     prev=pygame.K_RIGHT
                     direction = "RIGHT"

                elif event.key==pygame.K_UP and prev!=pygame.K_DOWN:
                    c_lead_y_change=-change_pos
                    c_lead_x_change =0
                    prev=pygame.K_UP
                    direction = "UP"

                elif event.key == pygame.K_DOWN and prev!=pygame.K_UP:
                    c_lead_y_change= change_pos
                    c_lead_x_change = 0
                    prev=pygame.K_DOWN
                    direction = "DOWN"
                elif event.key ==pygame.K_p:
                    pause()


        c_lead_x=c_lead_x+c_lead_x_change
        c_lead_y=c_lead_y+c_lead_y_change
        if c_lead_x>=display_length or c_lead_y>=display_height or c_lead_y<=0 or c_lead_x<=0 :
            game_over = True
        if ((c_lead_x>=randapplex and c_lead_y>=randappley)and(c_lead_x<=randapplex+apple_pos and c_lead_y<=randappley+apple_pos)):
                randapplex, randappley = apple_gen(apple_pos)
                score = score + 1
        clock.tick(20)
        gameDisplay.fill(white)
        screen_text = small_font.render("SCORE-", True, black)
        gameDisplay.blit(screen_text, [0,0])
        screen_text = small_font.render(str(score), True, black)
        gameDisplay.blit(screen_text, [100, 0])
        #pygame.draw.circle(gameDisplay, red, [int(randapplex),int(randappley)],apple_pos)
        gameDisplay.blit(apple_img, [int(randapplex),int(randappley)])
        snake_head = []
        snake_head.append(c_lead_x)
        snake_head.append(c_lead_y)
        snake_list.append(snake_head)
        if len(snake_list) > score:
            del snake_list[0]
        for eachsegment in snake_list[:-1]:
            if eachsegment == snake_head:
                game_over = True

        snake_print(snake_list,change_pos,direction)

        pygame.display.update()
    pygame.quit()
    quit()
game_start_screen()
gameloop()