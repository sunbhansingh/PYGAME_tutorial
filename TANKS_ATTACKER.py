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
cyan=(0,255,255)
light_cyan=(0,220,220)
ground_height=35
light_red=(255,0,0)
green=(34,175,40)
light_green=(0,255,0)
display_height=600
display_length=800
tank_height=20
tank_width=40
turret_width=5
vs_player=pygame.image.load('blue_img.jpg')
losing_game=pygame.image.load('losing_game.png')
grass_image=pygame.image.load('grass.jpg')
back_image=pygame.image.load('wallpaper.jpg')
fire_sound = pygame.mixer.Sound("shot.wav")
explosion_sound = pygame.mixer.Sound("explosion.wav")
pygame.mixer.music.load("back_music.wav")
pygame.mixer.music.play(-1)
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
                choosing_player_enemy()
            if action=="Control":
                controls_menu()
            if action=="Quit":
                pygame.quit()
                quit()
            if action=="Main":
                game_start_screen()
            if action=="VS_PLAYER":
                gameloop_player()
            if action=="VS_ENEMY":
                gameloop()
    else:
        pygame.draw.rect(gameDisplay,passive_color,(box_x,box_y,box_width,box_height))
        text_to_box(msg,box_x,box_y,box_width,box_height,size,black)
def text_to_box(msg,box_x,box_y,box_width,box_height,size,color):
    screen_text=size.render(msg,True,color)
    text_rect=screen_text.get_rect()
    text_rect.center=(int(box_x+box_width/2),int(box_y+box_height/2))
    gameDisplay.blit(screen_text,text_rect)
def pause():
    pygame.mixer.music.stop()
     
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
def message_to_screen(msg,color,y_displace=0,size="small_font" ):
    screen_text=size.render(msg,True,color)
    text_rect=screen_text.get_rect()
    text_rect.center=display_length/2,display_height/2+y_displace
    gameDisplay.blit(screen_text,text_rect)
def game_start_screen():
    gameDisplay.fill(white)
    gameDisplay.blit(back_image,[0,0])
    flag=True
    message_to_screen("Welcome to Tank attackers",cyan,-190,medium_font)
    message_to_screen("Attack enemies using ur powers and finish them", red, -120, small_font)
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
def game_over_2(WHO_WON):
    pygame.mixer.music.stop()
    gameDisplay.fill(white)
     
    #gameDisplay.blit(losing_game,[0,0])
    flag=True
    message_to_screen("YOU LOSE",green,-50,medium_font)
    message_to_screen(str(str(WHO_WON)+"fucked u"), red, 0, small_font)
    pygame.display.update()
    while flag:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        button("Restart",150,500,100,50,small_font,green,light_green,action="Play")
        button("Control",350,500,100,50,small_font,yellow,light_yellow,action="Control")      
        button("Quit",550,500,100,50,small_font,red,light_red,action="Quit")      
        pygame.display.update()
        clock.tick(50)
def player_win():
    pygame.mixer.music.stop()
    gameDisplay.fill(white)
    flag=True
    message_to_screen("YOU WIN",green,-50,medium_font)
    message_to_screen("you fucked enemy", red, 0, small_font)
    while flag:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        button("Restart",150,500,100,50,small_font,green,light_green,action="Play")
        button("Control",350,500,100,50,small_font,yellow,light_yellow,action="Control")      
        button("Quit",550,500,100,50,small_font,red,light_red,action="Quit")      
        pygame.display.update()
        clock.tick(50)            

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
        counte=counte-1
    return turrets_end_coordinates[turrets_pos]
def enemy_tank(x,y,color,turrets_pos):
    x=int(x)
    y=int(y)
    turret_width=5
    turrets_end_coordinates=[(x+27, y-2),(x+26, y-5),(x+25, y-8),(x+23, y-12),(x+20, y-14),(x+18, y-15),(x+15, y-17),(x+13, y-19),(x+11, y-21)]
    pygame.draw.circle(gameDisplay,color,(x,y),int(tank_height/2))
    pygame.draw.rect(gameDisplay,color,(x-tank_width/2,y,tank_width,tank_height))
    pygame.draw.line(gameDisplay,color,(x,y),turrets_end_coordinates[turrets_pos],turret_width)
    start_x=15
    counte=7
    while counte!=0:
        pygame.draw.circle(gameDisplay,color,((int(x-int(tank_width/2)*0)-start_x),(y+tank_height)),tank_wheel_radius)
        start_x=start_x-5
        counte=counte-1
    return turrets_end_coordinates[turrets_pos]
def explosion(hit_x,hit_y,size):
    pygame.mixer.Sound.play(explosion_sound)
    explo=True
    loop=20
    colors=[white,blue,yellow,light_yellow,black,red,light_red,green,light_green]
    while explo:
        pygame.draw.circle(gameDisplay,colors[random.randrange(-1,8)],(hit_x+random.randrange(size),hit_y-random.randrange(size)),4)
        loop-=1
        if loop==0:
            explo=False
def gun_fire(xy,gun_power,turPos,fire_power,barrier_x,barrier_y,barrier_width,barrier_height,tank,main_tank_x,dest_x,health):
    pygame.mixer.Sound.play(fire_sound)
    fire=True
    changing_coordinates=list(xy)
    while fire:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
        pygame.draw.circle(gameDisplay, green, (changing_coordinates[0],changing_coordinates[1]),5)
        if tank=="self":
            changing_coordinates[0] -= (12 - turPos)*2
        elif tank=="PLAYER_2":
            changing_coordinates[0]+=(12-turPos)*2
        # y = x**2
        changing_coordinates[1] += int((((changing_coordinates[0]-xy[0])*(0.015/(fire_power/50))/(gun_power/50))**2) - (turPos+turPos/(12-turPos)))
        check1=(barrier_x+barrier_width>=changing_coordinates[0])
        check2=(changing_coordinates[0]>barrier_x)
        check3=(changing_coordinates[1]<=display_height)
        check4=(barrier_y<=changing_coordinates[1])
        if changing_coordinates[1]>display_height-ground_height or changing_coordinates[1]<0 or changing_coordinates[0]<0:
            fire=False
            hit_x=int((changing_coordinates[0]/changing_coordinates[1])*(display_height-ground_height))#((x/y)=(x/y))
            hit_y=display_height-ground_height
            explosion(hit_x,hit_y,20)
            if dest_x+25>hit_x>dest_x-25:
                print("enemy damage"+str(((abs(hit_x-dest_x)))))
                health=health-(abs(hit_x-dest_x))
        elif (check1 and check2 and check3 and check4):
            explosion(changing_coordinates[0],changing_coordinates[1],20)
            fire=False
        pygame.display.update()
        clock.tick(50)
    return health    
def enemy_gun_fire(xy,gun_power,turPos,barrier_x,barrier_y,barrier_width,barrier_height,tank,main_tank_x,health):
    pygame.mixer.Sound.play(fire_sound)
    fire=True
    fire_power=1
    while fire:
        fire_power+=1
        if fire_power>100:
            fire=False
        changing_coordinates=list(xy)
        dest=True
        while dest:
            changing_coordinates[0] += (12 - turPos)*2
            # y = x**2
            changing_coordinates[1] += int((((changing_coordinates[0]-xy[0])*(0.015/(fire_power/50))/(gun_power/50))**2) - (turPos+turPos/(12-turPos)))
            check1=(barrier_x+barrier_width>=changing_coordinates[0])
            check2=(changing_coordinates[0]>barrier_x)
            check3=(changing_coordinates[1]<=display_height)
            check4=(barrier_y<=changing_coordinates[1])
            if changing_coordinates[1]>display_height-ground_height:
                hit_x=int((changing_coordinates[0]/changing_coordinates[1])*(display_height-ground_height))#((x/y)=(x/y))
                hit_y=display_height-ground_height
                if main_tank_x+15>hit_x>main_tank_x-15:
                    print("player damage"+str(abs(hit_x-main_tank_x)))
                    health=health-(abs(hit_x-main_tank_x))
                    fire=False
                    pygame.display.update()
                    clock.tick(50)
                dest=False
            if check1 and check2 and check3 and check4:
                dest=False
    dest=True
    fire=True
    changing_coordinates=list(xy)
    while fire:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
        pygame.draw.circle(gameDisplay, green, (changing_coordinates[0],changing_coordinates[1]),5)
        changing_coordinates[0] += (12 - turPos)*2
        # y = x**2
        changing_coordinates[1] += int((((changing_coordinates[0]-xy[0])*(0.015/(fire_power/50))/(gun_power/50))**2) - (turPos+turPos/(12-turPos)))
        check1=(barrier_x+barrier_width>=changing_coordinates[0])
        check2=(changing_coordinates[0]>barrier_x)
        check3=(changing_coordinates[1]<=display_height)
        check4=(barrier_y<=changing_coordinates[1])
        if changing_coordinates[1]>display_height-ground_height or changing_coordinates[1]<0 or changing_coordinates[0]<0:
            fire=False
            hit_x=int((changing_coordinates[0]/changing_coordinates[1])*(display_height-ground_height))#((x/y)=(x/y))
            hit_y=display_height-ground_height
            explosion(hit_x,hit_y,20)
        elif (check1 and check2 and check3 and check4):
            explosion(changing_coordinates[0],changing_coordinates[1],20)
            fire=False
        pygame.display.update()
        clock.tick(50)
    return health    
def health_bar(player_health,x,y):
    if player_health>75:
        color=green
    elif player_health>25:
        color=yellow
    elif player_health>0:
        color=red
    else:
        return;
    pygame.draw.rect(gameDisplay,color,(x,y,player_health,25))
def barrier(barrier_x,barrier_y,barrier_width,barrier_height,color):
    pygame.draw.rect(gameDisplay,color,(barrier_x,barrier_y,barrier_width,barrier_height))
def choosing_player_enemy():
    hold_screen=True
    while hold_screen:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            gameDisplay.fill(cyan)    
            
            button("VS PLAYER",350,200,150,50,small_font,cyan,light_cyan,action="VS_PLAYER")
            button("VS ENEMY",350,300,150,50,small_font,cyan,light_cyan,action="VS_ENEMY")   
            pygame.display.update()    
            clock.tick(30)
        
def gameloop():
    pygame.mixer.music.stop()
    pygame.mixer.music.load("ingame.wav")
    pygame.mixer.music.play(-1)
    tank_move=0
    barrier_width=40
    player_health=100
    enemy_health=100
    barrier_x=random.randrange(int(.20*display_length),int(.60*display_length))
    barrier_y=random.randrange(int(.5*display_height),int(.8*display_height))
    fire_power=50
    final_turret_pos=0
    enemy_final_turret_pos=8
    turret_pos=0
    FPS=15
    power=0
    fire_power=50
    final_tank_move=0
    main_tank_x=(0.9*display_length)
    main_tank_y=(0.9*display_height)
    enemy_main_tank_x=(0.1*display_length)
    enemy_main_tank_y=(0.9*display_height)
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
                if event.key==pygame.K_LEFT :
                    tank_move=-5
                elif event.key==pygame.K_d:
                    power=1
                elif event.key==pygame.K_a:
                    power=-1
                elif event.key==pygame.K_RIGHT and main_tank_x+int(tank_width/2)<display_length:
                    tank_move=5
                elif event.key==pygame.K_UP:
                    turret_pos=1
                elif event.key == pygame.K_DOWN:
                    turret_pos=-1
                elif event.key ==pygame.K_p:
                    pause()
                    pygame.mixer.music.load("ingame.wav")
                    pygame.mixer.music.play(-1)
                                        
                elif event.key==pygame.K_SPACE:
                    enemy_health=gun_fire(starting_fire_coordinates,80,final_turret_pos,fire_power,barrier_x,barrier_y,barrier_width,barrier_height,"self",main_tank_x,enemy_main_tank_x,enemy_health)
                    player_health=enemy_gun_fire(enemy_starting_fire_coordinates,80,enemy_final_turret_pos,barrier_x,barrier_y,barrier_width,barrier_height,"enemy",main_tank_x,player_health)
                    #moving enemy tank
                    directions=['f','r']
                    d=random.randrange(2)
                    for x in range(random.randrange(10)):
                        if ( int(display_length*(.5))>enemy_main_tank_x>int((display_length*.05))): 
                            if directions[d]=='f' and enemy_main_tank_x<int(.3*display_length):
                                enemy_main_tank_x+=5
                            elif directions[d]=='r' and enemy_main_tank_x-int(tank_width/2)>0:
                                enemy_main_tank_x-=5
                            gameDisplay.fill(white)
                            gameDisplay.blit(grass_image,[0,0])
                            health_bar(player_health,680,25)
                            health_bar(enemy_health,25,25)
                            if main_tank_x+int(tank_width/2)<display_length:
                                starting_fire_coordinates=tank(main_tank_x,main_tank_y,red,final_turret_pos)
                            enemy_starting_fire_coordinates=enemy_tank(enemy_main_tank_x,enemy_main_tank_y,green,enemy_final_turret_pos)
                            barrier_height=(display_height-barrier_y)
                            barrier(barrier_x,barrier_y,barrier_width,barrier_height-ground_height,black)
                            final_turret_pos+=turret_pos
                            #gameDisplay.fill(green, rect=[0, display_height-ground_height, display_length, ground_height])
                            message_to_screen("Power ="+str(fire_power),black,-280,small_font)
                            pygame.display.update()
                            clock.tick(FPS)
            elif event.type==pygame.KEYUP:
                if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
                    tank_move=0
                if event.key==pygame.K_UP or event.key==pygame.K_DOWN:
                    turret_pos=0
                if event.key==pygame.K_a or event.key==pygame.K_d:
                    power=0
        if player_health<1:
            game_over_2("ENEMY")
        elif enemy_health<1:
            player_win()
        fire_power+=power
        if fire_power>100:
            fire_power=100
        elif fire_power<0:
            fire_power=0
        if final_turret_pos>8:
            final_turret_pos=8
        elif final_turret_pos<0:
            final_turret_pos=0
        main_tank_x+=tank_move
        gameDisplay.fill(white)
        gameDisplay.blit(grass_image,[0,0])
        health_bar(player_health,680,25)
        health_bar(enemy_health,25,25)
        if main_tank_x+int(tank_width/2)>display_length:
            main_tank_x=abs(int(tank_width/2)-display_length)
        starting_fire_coordinates=tank(main_tank_x,main_tank_y,red,final_turret_pos)
        enemy_starting_fire_coordinates=enemy_tank(enemy_main_tank_x,enemy_main_tank_y,green,enemy_final_turret_pos)
        barrier_height=(display_height-barrier_y)
        barrier(barrier_x,barrier_y,barrier_width,barrier_height-ground_height,black)
        final_turret_pos+=turret_pos
        #gameDisplay.fill(green, rect=[0, display_height-ground_height, display_length, ground_height])
        message_to_screen("Power ="+str(fire_power),black,-280,small_font)
        pygame.display.update()
        clock.tick(FPS)
    pygame.quit()
    quit()
def gameloop_player():
    pygame.mixer.music.stop()
    pygame.mixer.music.load("ingame.wav")
    pygame.mixer.music.play(-1)
    tank_move=0
    barrier_width=40
    player_health=100
    enemy_health=100
    barrier_x=random.randrange(int(.20*display_length),int(.60*display_length))
    barrier_y=random.randrange(int(.5*display_height),int(.8*display_height))
    fire_power=50
    final_turret_pos=0
    enemy_final_turret_pos=0
    enemy_turret_pos=0
    enemy_tank_move=0
    turret_pos=0
    FPS=15
    power=0
    fire_power=50
    final_tank_move=0
    main_tank_x=(0.9*display_length)
    main_tank_y=(0.9*display_height)
    enemy_main_tank_x=(0.1*display_length)
    enemy_main_tank_y=(0.9*display_height)
    gameexit=False
    game_over=False
    while not gameexit:
        
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                gameexit=True
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_LEFT :
                    tank_move=-5
                elif event.key==pygame.K_j:
                    power=1
                elif event.key==pygame.K_l:
                    power=-1
                elif event.key==pygame.K_RIGHT and main_tank_x+int(tank_width/2)<display_length:
                    tank_move=5
                elif event.key==pygame.K_UP:
                    turret_pos=1
                elif event.key == pygame.K_DOWN:
                    turret_pos=-1
                elif event.key ==pygame.K_p:
                    pause()
                    pygame.mixer.music.load("ingame.wav")
                    pygame.mixer.music.play(-1)
                elif event.key==pygame.K_SPACE:
                    enemy_health=gun_fire(starting_fire_coordinates,80,final_turret_pos,fire_power,barrier_x,barrier_y,barrier_width,barrier_height,"self",main_tank_x,enemy_main_tank_x,enemy_health)
                    
                    loop=True
                    while loop:
                        for event in pygame.event.get():
                            if event.type==pygame.QUIT:
                                pygame.quit()
                                quit()
                            if event.type==pygame.KEYDOWN:
                                if event.key==pygame.K_a :
                                    enemy_tank_move=-5
                                elif event.key==pygame.K_d:
                                    enemy_tank_move=5
                                elif event.key==pygame.K_w:
                                    enemy_turret_pos=1
                                elif event.key==pygame.K_s:    
                                    enemy_turret_pos=-1
                                elif event.key==pygame.K_j:
                                    power=1
                                elif event.key==pygame.K_l:
                                    power=-1
                                elif event.key==pygame.K_SPACE:
                                    player_health=gun_fire(enemy_starting_fire_coordinates,80,enemy_final_turret_pos,fire_power,barrier_x,barrier_y,barrier_width,barrier_height,"PLAYER_2",enemy_main_tank_x,main_tank_x,player_health)
                                  #  (xy,gun_power,turPos,fire_power,barrier_x,barrier_y,barrier_width,barrier_height,tank,main_tank_x,dest_x,health):
                                    
                                    loop=False
                            if event.type==pygame.KEYUP:
                                if event.key==pygame.K_a or event.key==pygame.K_d:
                                    enemy_tank_move=0
                                elif event.key==pygame.K_w or event.key==pygame.K_s:
                                    enemy_turret_pos=0
                                elif event.key==pygame.K_j or event.key==pygame.K_l:
                                    power=0
                        fire_power+=power
                        enemy_main_tank_x+=enemy_tank_move
                        enemy_final_turret_pos+=enemy_turret_pos
                        if fire_power>100:
                            fire_power=100
                        elif fire_power<0:
                            fire_power=0
                        if enemy_final_turret_pos>8:
                            enemy_final_turret_pos=8
                        elif enemy_final_turret_pos<0:
                            enemy_final_turret_pos=0
                        if enemy_main_tank_x-int(tank_width/2)<0:
                            enemy_main_tank_x=int(tank_width/2)
                        gameDisplay.fill(white)
                        gameDisplay.blit(grass_image,[0,0])
                        health_bar(player_health,680,25)
                        health_bar(enemy_health,25,25)
                        starting_fire_coordinates=tank(main_tank_x,main_tank_y,red,final_turret_pos)
                        
                        enemy_starting_fire_coordinates=enemy_tank(enemy_main_tank_x,enemy_main_tank_y,green,enemy_final_turret_pos)
                        barrier_height=(display_height-barrier_y)
                        barrier(barrier_x,barrier_y,barrier_width,barrier_height-ground_height,black)
                                                
                        message_to_screen("Power ="+str(fire_power),black,-280,small_font)
                        pygame.display.update()
                        clock.tick(FPS)
                       
            elif event.type==pygame.KEYUP:
                if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
                    tank_move=0
                if event.key==pygame.K_UP or event.key==pygame.K_DOWN:
                    turret_pos=0
                if event.key==pygame.K_j or event.key==pygame.K_l:
                    power=0
                if event.key==pygame.K_a or event.key==pygame.K_d:
                    enemy_tank_move=0
                if event.key==pygame.K_w or event.key==pygame.K_s:
                    enemy_turret_pos=0
        if player_health<1:
            game_over_2("PLAYER 2")
        elif enemy_health<1:
            player_win()
        fire_power+=power
        if fire_power>100:
            fire_power=100
        elif fire_power<0:
            fire_power=0
        if final_turret_pos>8:
            final_turret_pos=8
        elif final_turret_pos<0:
            final_turret_pos=0
        if enemy_final_turret_pos>8:
            enemy_final_turret_pos=8
        elif enemy_final_turret_pos<0:
            enemy_final_turret_pos=0
        main_tank_x+=tank_move
        enemy_main_tank_x+=enemy_tank_move
        gameDisplay.fill(white)
        gameDisplay.blit(grass_image,[0,0])
        health_bar(player_health,680,25)
        health_bar(enemy_health,25,25)
        if main_tank_x+int(tank_width/2)>display_length:
            main_tank_x=abs(int(tank_width/2)-display_length)
        if enemy_main_tank_x-int(tank_width/2)<0:
            enemy_main_tank_x=int(tank_width/2)
        
        starting_fire_coordinates=tank(main_tank_x,main_tank_y,red,final_turret_pos)
        enemy_starting_fire_coordinates=enemy_tank(enemy_main_tank_x,enemy_main_tank_y,green,enemy_final_turret_pos)
        barrier_height=(display_height-barrier_y)
        barrier(barrier_x,barrier_y,barrier_width,barrier_height-ground_height,black)
        final_turret_pos+=turret_pos
        enemy_final_turret_pos+=enemy_turret_pos
        
        #gameDisplay.fill(green, rect=[0, display_height-ground_height, display_length, ground_height])
        message_to_screen("Power ="+str(fire_power),black,-280,small_font)
        pygame.display.update()
        clock.tick(FPS)
    pygame.quit()
    quit()
    
game_start_screen()
