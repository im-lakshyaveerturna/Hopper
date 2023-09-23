import pygame
from sys import exit
from random import randint


def obstacle_movement(obstacle_list):
    if obstacle_list: 
        for obstacle_rect in obstacle_list:
            obstacle_rect.x -= 5
            if obstacle_rect.bottom == 307:
               screen.blit(zombie, obstacle_rect)

            else: 
                screen.blit(bat, obstacle_rect)

        obstacle_list = [obstacle for obstacle in obstacle_list if obstacle.x > -100]
        return obstacle_list

    else: return []

def collision(runner,obstacles ):
        if obstacles:
             for obstacle_rect in obstacles:
                 
        
                 if runner.colliderect(obstacle_rect):
                     
                     return False 
                     

        return True

                    
def display_score(): 
    time = int(pygame.time.get_ticks()/100) - int(start_time/100)
    score = font.render(f'Score: {time}', False, 'Orange')

                
    score_rect = score.get_rect(center = (400,50))
    screen.blit(score, score_rect)
    return time

def player_animations():
    global runner, index
    if runner_rect.bottom < 307:
        runner = jump

    else:
        index += 0.1
        
        if index >= len(runner_run):
            index = 0
        runner = runner_run[int(index)]


    

       

pygame.init()
start_time = 0
game_active = True
screen = pygame.display.set_mode((800, 400))
bg = pygame.image.load('downloads/hopperbg.jpeg').convert_alpha()
bg1 = pygame.transform.scale(bg, (800, 400))
gscore = 0

font = pygame.font.Font(None, 75)

#Obstacles:

enemy = pygame.image.load('downloads/pyrat.png').convert_alpha()
zombie = pygame.transform.scale(enemy, (75,75))
pybat = pygame.image.load('downloads/pybat.png').convert_alpha()
bat = pygame.transform.scale(pybat, (50,50)) 
obstacle_rect_list = [] 


#Timer:
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer,2000)


#Main character:-
pyrunner = pygame.image.load('downloads/runner.png').convert_alpha()
runner1 = pygame.transform.scale(pyrunner, (75,75))
pyrunner2 = pygame.image.load('downloads/runner2.png').convert_alpha()
runner2 = pygame.transform.scale(pyrunner2, (75,75))

runner_run = [runner1,runner2]
index = 0
jump = pygame.image.load('downloads/jump.png').convert_alpha()
runner = runner_run[int(index)]
runner_rect = runner.get_rect(midright = (150, 307) )

runner_g = 0
runner_stand = pygame.image.load('downloads/pyrunner.png').convert_alpha()
runner_stand1 = pygame.transform.scale(pyrunner, (150,150))
runnner_stand1_rect = runner_stand1.get_rect(midbottom = (400, 307))

#Music

pygame.mixer.Sound('downloads/hopperbgsound.mp3')

pygame.display.set_caption('Hopper')

clock = pygame.time.Clock()

while True:
    bgsound = pygame.mixer.Sound('downloads/hopperbgsound.mp3')
    bgsound.play()
 #Key conrols:-    
    for event in pygame.event.get():
        if event.type ==  pygame.QUIT:
            pygame.quit()
            exit()
        if game_active:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and runner_rect.bottom >= 307 :

                
                    runner_g = -25
                    jsound = pygame.mixer.Sound('downloads/hopperbgsound.mp3')
                    jsound.play()


                    

            

        

        else: 
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                
                start_time =  pygame.time.get_ticks()


        #Timer:-

        if event.type == obstacle_timer and game_active:
            if randint(0,2) == 1:
            
              obstacle_rect_list.append(bat.get_rect(midbottom = (randint(900,1100),200)))
            
            else:
                obstacle_rect_list.append(zombie.get_rect(midbottom = (randint(900,1100),307)))
 
                    






    if game_active:
            #Screen Blits
            screen.blit(bg1,(0,0))
            gscore = display_score()


            #Gravity
            runner_g +=1
            runner_rect.y += runner_g


            if runner_rect.bottom >= 307:
                runner_rect.bottom =307
            player_animations()
            screen.blit(runner,runner_rect )


        


           #Collision
           
            game_active = collision(runner_rect, obstacle_rect_list)           
            obstacle_rect_list = obstacle_movement(obstacle_rect_list)

    else:

        
       
        obstacle_rect_list.clear()
        runner_rect.midbottom = (150,307)
        screen.fill((94, 129, 162))
        go = font.render('GAME OVER', False, 'Orange')
        go_rect = go.get_rect(midbottom = (400, 70))
        screen.blit(go, go_rect)

        runner_stand = pygame.image.load('downloads/pyrunner.png').convert_alpha()
        runner_standa = pygame.transform.scale(pyrunner, (150,150))
        runner_standa_rect = runner_stand1.get_rect(midbottom = (385, 350))
        screen.blit(runner_standa, runner_standa_rect )

        ascore = font.render(f'Score: {gscore}', False, 'Orange')
        ascore_rect = ascore.get_rect(midbottom = (400, 180))
        screen.blit(ascore, ascore_rect)

        font2 = pygame.font.Font(None,25 )
        ins = font2.render("Press 'space' key to play again", False, "Orange")
        ins_rect = ins.get_rect(midbottom = (400,390))
        screen.blit(ins, ins_rect)
        soman = True
        time2 = pygame.time.get_ticks()/1000
        
        




                
                        


    pygame.display.update()
    clock.tick(60)
     