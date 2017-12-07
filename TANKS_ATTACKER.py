import pygame
import time
import random
pygame.init()
clock=pygame.time.Clock()
white=(255,255,255)
blue=(0,0,1)
yellow=(255,250,0)
light_yellow=(200,200,0)
black=(0,0,0)
red=(200,0,0)
light_red=(255,0,0)
green=(34,175,40)
light_green=(0,255,0)
display_height=600
display_length=800
tank_height=20
tank_width=40
turret_width=5
tank_wheel_radius=int(tank_height*.25)
small_font=pygame.font.SysFont("comicsansms",25)
medium_font=pygame.font.SysFont("comicsansms",50)
large_font=pygame.font.SysFont("comicsansms",75)
gameDisplay=pygame.display.set_mode((display_length,display_height))
pygame.display.set_caption("bhan_game")
def controls_menu():
    gameDisplay.fill(white)
    flag=True
    message_to_screen("Controls",green,-50,medium_font)
    message_to_screen("moving the tank            <-  and    ->", red, 0, small_font)
    message_to_screen("shooting powers                space bar", red, 25, small_font)
    message_to_screen("Pause                                  P", red, 50, small_font)
    while flag:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            button("Play",150,500,100,50,small_font,green,light_green,action="Play")
            button("Quit",550,500,100,50,small_font,red,light_red,action="Quit")      
            button("Main",350,500,100,50,small_font,yellow,light_yellow,action="Main")
                        
            pygame.display.update()
            clock.tick(50)            
    
    pygame.display.update()
           
def button(msg,box_x,box_y,box_width,box_height,size,passive_color,active_color,action=None): 
    curr=pygame.mouse.get_pos()
    if ((curr[0]>=box_x and curr[0]<=box_x+box_width) and (curr[1]>=box_y and curr[1]<=box_y+box_height)):
        click=pygame.mouse.get_pressed()
        pygame.draw.rect(gameDisplay,active_color,(box_x,box_y,box_width,box_height))
        text_to_box(msg,box_x,box_y,box_width,box_height,size,black)
        if click[0]==1 and action!=None:
            if action=="Play":    
                gameloop()
            if action=="Control":
                print("hello")
                controls_menu()
            if action=="Quit":
                pygame.quit()
                quit()
            if action=="Main":
                game_start_screen()
            
    else:
        pygame.draw.rect(gameDisplay,passive_color,(box_x,box_y,box_width,box_height))
        text_to_box(msg,box_x,box_y,box_width,box_height,size,black)
def text_to_box(msg,box_x,box_y,box_width,box_height,size,color):
    screen_text=size.render(msg,True,color)
    text_rect=screen_text.get_rect()
    text_rect.center=(int(box_x+box_width/2),int(box_y+box_height/2))
    gameDisplay.blit(screen_text,text_rect)
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
def game_start_screen():
    gameDisplay.fill(white)
    flag=True
    message_to_screen("Welcome to Tank attackers",green,-50,medium_font)
    message_to_screen("Attack enemies using ur powers and finish them", red, 0, small_font)
    
    while flag:
        
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
            
            button("Play",150,500,100,50,small_font,green,light_green,action="Play")
            button("Control",350,500,100,50,small_font,yellow,light_yellow,action="Control")      
            button("Quit",550,500,100,50,small_font,red,light_red,action="Quit")      
            
            pygame.display.update()
            clock.tick(50)            
def message_to_screen(msg,color,y_displace=0,size="small_font" ):
    screen_text=size.render(msg,True,color)
    text_rect=screen_text.get_rect()
    text_rect.center=display_length/2,display_height/2+y_displace
    gameDisplay.blit(screen_text,text_rect)
def tank(x,y,color,turrets_pos):
    x=int(x)
    y=int(y)
    turret_width=5
    turrets_end_coordinates=[(x-27, y-2),(x-26, y-5),(x-25, y-8),(x-23, y-12),(x-20, y-14),(x-18, y-15),(x-15, y-17),(x-13, y-19),(x-11, y-21)]
    pygame.draw.circle(gameDisplay,color,(x,y),int(tank_height/2))
    pygame.draw.rect(gameDisplay,color,(x-tank_width/2,y,tank_width,tank_height))
    pygame.draw.line(gameDisplay,color,(x,y),turrets_end_coordinates[turrets_pos],turret_width)
    start_x=15
    counte=7
    while counte!=0:
        pygame.draw.circle(gameDisplay,color,((int(x-int(tank_width/2)*0)-start_x),(y+tank_height)),tank_wheel_radius)
        start_x=start_x-5
        pygame.display.update()
        counte=counte-1
def barrier(barrier_x,barrier_y,barrier_width,barrier_height,color):
    pygame.draw.rect(gameDisplay,color,(barrier_x,barrier_y,barrier_width,barrier_height))
    pygame.display.update()
    
def gameloop():
    tank_move=0
    barrier_x=random.randrange(int(.20*display_length),int(.60*display_length))
    barrier_y=random.randrange(int(.5*display_height),int(.8*display_height))
    
    final_turret_pos=0
    turret_pos=0
    final_tank_move=0
    main_tank_x=(0.9*display_length)
    main_tank_y=(0.9*display_height)
    gameDisplay.fill(white)
    gameexit=False
    game_over=False
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
        
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                gameexit=True
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_LEFT:
                    tank_move=-5 
                elif event.key==pygame.K_RIGHT:
                    tank_move=5
                elif event.key==pygame.K_UP:
                    turret_pos=1
                elif event.key == pygame.K_DOWN:
                    turret_pos=-1
                elif event.key ==pygame.K_p:
                    pause()
            elif event.type==pygame.KEYUP:
                if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
                    tank_move=0
                if event.key==pygame.K_UP or event.key==pygame.K_DOWN:
                    turret_pos=0
        gameDisplay.fill(white)
        for x in range(15):
            barrier_height=(display_height-barrier_y)
            barrier_width=40
            barrier(barrier_x,barrier_y,barrier_width,barrier_height,black)
                      
        final_turret_pos+=turret_pos
        if final_turret_pos>8:
            final_turret_pos=8
        elif final_turret_pos<0:
            final_turret_pos=0
        main_tank_x+=tank_move
        tank(main_tank_x,main_tank_y,red,final_turret_pos)
        pygame.display.update()
        clock.tick(5)
    pygame.quit()
    quit()
game_start_screen()
