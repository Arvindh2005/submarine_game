import pygame
import time
import random
import math

#270(approx) - submarine_width ,154 - submarine_height , 133 , 60
# DISPLAY SCREEN
pygame.init()
fpsclock = pygame.time.Clock()
pygame.display.set_caption("  SUBMARINE CHALLENGE  ")
icon = pygame.image.load("ALWAYSRR.ico")
pygame.display.set_icon(icon)
width = 1000
height = 600

score_last = 0

pause = -1

# GRENADE RESEARCH
grenade_img = pygame.image.load("grenade.png")
grenade_state = "reserve"
grenadey = -100
grenadex = 0
grenade_code = -1
grenade_activation = -1
grenade_identifier = -1
grenade_mask = pygame.mask.from_surface(grenade_img)

# DANGER SIGN
danger_sign = pygame.image.load("danger.png")
dangerx = grenadex
dangery = 20

explosion = pygame.image.load("explosion_bomb.png")
explosionx = 10000
explosiony = 10000

A = 853
CF = 0

submarine_input = -1

# SCREEN OPTIMISATION
screen = pygame.display.set_mode((width,height))
background = pygame.image.load("underwater.jpg").convert()
background = pygame.transform.scale(background , (2000,1200))

activate = -1

#SUBMARINE
submarine = pygame.image.load("submarine.png")
submarine_width = submarine.get_width()
submarine_height = submarine.get_height()
submarinex = 100
submariney = 100
submarinexch = 0
submarineych = 0
submarine_mask = pygame.mask.from_surface(submarine)
submarine_rect = submarine.get_rect()
submarine_health = 200
submarine_fuel = 100
fuel_monitor = 0

AB = time.time()

mousex = 0
mousey = 0

# GUN
gun_img = pygame.image.load("game_gun1.png")
gun_width = gun_img.get_width()
gun_height = gun_img.get_height()
gun_img = pygame.transform.scale(gun_img , (gun_width//2 , gun_height//2))

gunx1 = 900
guny1 = 40

gunx2 = 900
guny2 = 120

gunx3 = 900
guny3 = 200

gunx4 = 900
guny4 = 280

gunx5 = 900
guny5 = 360

gunx6 = 900
guny6 = 440

gunx7 = 900
guny7 = 520

# POWERUP RESEARCH - AI POWERED POWERUP_BOX GENERATOR

power_up = pygame.image.load("powerup.png")
powerupx = 4000
powerupy = 100
power_up_generator = -1
power_up_mask = pygame.mask.from_surface(power_up)
powerupxch = 0

fuel = pygame.image.load("tank.png")
fuelx = 4000
fuely = 100
fuelxch = 0
fuel_mask = pygame.mask.from_surface(fuel)

# BULLET
bulletx1 = -100
bulletx2 = -100
bulletx3 = -100
bulletx4 = -100
bulletx5 = -100
bulletx6 = -100
bulletx7 = -100

bullety1 = 61
bullety2 = 141
bullety3 = 221
bullety4 = 301
bullety5 = 381
bullety6 = 461
bullety7 = 541

random_nos = 1
active = -1

bullet_img1 = pygame.image.load("game_bullets.png")
bullet_mask1 = pygame.mask.from_surface(bullet_img1)
bullet1_state = "Reserve"
bullet_rect1 = bullet_img1.get_rect()

bullet_img2 = pygame.image.load("game_bullet.png")
bullet_mask2 = pygame.mask.from_surface(bullet_img2)
bullet2_state = "Reserve"

bullet_img3 = pygame.image.load("game_bulletss.png")
bullet_mask3 = pygame.mask.from_surface(bullet_img3)
bullet3_state = "Fire"

bullet_img4 = pygame.image.load("game_bullet.png")
bullet_mask4 = pygame.mask.from_surface(bullet_img4)
bullet4_state = "Reserve"

bullet_img5 = pygame.image.load("game_bullets.png")
bullet_mask5 = pygame.mask.from_surface(bullet_img5)
bullet5_state = "Reserve"

bullet_img6 = pygame.image.load("game_bulletss.png")
bullet_mask6 = pygame.mask.from_surface(bullet_img6)
bullet6_state = "Reserve"

bullet_img7 = pygame.image.load("game_bullet.png")
bullet_mask7 = pygame.mask.from_surface(bullet_img7)
bullet7_state = "Reserve"

retry = pygame.image.load("retry.png")

nuclear = pygame.image.load("nuclear_bomb.png")

nucleargun = pygame.image.load("gunspl.png")

tiles = math.ceil(1000/1000)
scroll = 0
CD = 0 
EF = 0
times = 0

bg_generator = 1
bg_code = 0

submarine_input_past = 1

def bg_generating_machine():
    global bg_generator
    bg_generator = random.randint(1,4)

def random_no():
    global random_nos
    random_nos = random.randint(1,7)

def grenade_activator():
    global grenade_code
    grenade_code = random.randint(1 , 3)

def submarine_generator():
    submarine_code = random.randint(1,5)
    return submarine_code

def timer():
    global CD
    CD = time.time()

run = True
speed = 11

font = pygame.font.Font(None , 40)

def writing_font():
    text = font.render("Score : " + str(int(EF)) , 1 , (0,0,0))
    screen.blit(text , (700 , 20))

def writing_font1():
    text = font.render("Score : " + str(int(score_last)) , 1 , (0,0,0))
    screen.blit(text , (700 , 20))

while run :

    fpsclock.tick(60)

    screen.fill((0,0,0))
    times = pygame.time.get_ticks()
    
    # GAME ACTIVITY

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if submariney >= 5:
                    submarineych = -6
                    if int(EF) >= 60 and int(EF) <= 120:
                        submarineych = -7 
                    if int(EF) > 120 and int(EF) <= 180 :
                        submarineych = -9
                    if int(EF) > 180 :
                        submarineych = -11
                
            if event.key == pygame.K_RIGHT:
                if submarinex <= 583 :
                    submarinexch = 5
                    
            if event.key == pygame.K_DOWN:
                if submariney <= 440:
                    submarineych = 6
                    if int(EF) >= 60 and int(EF) <= 120:
                        submarineych = 7 
                    if int(EF) > 120 and int(EF) <= 180 :
                        submarineych = 9
                    if int(EF) > 180 :
                        submarineych = 11
                        
            if event.key == pygame.K_LEFT:
                if submarinex >= 10 :
                    submarinexch = -5
            
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP :
                submarineych = 0
            if event.key == pygame.K_RIGHT:
                submarinexch = 0
            if event.key == pygame.K_DOWN:
                submarineych = 0
            if event.key == pygame.K_LEFT:
                submarinexch = 0

        if event.type == pygame.MOUSEBUTTONUP and activate != -1:
            print("hi")

        if event.type == pygame.MOUSEBUTTONUP and activate == -1:
            activate = 0
            timer()

        if event.type == pygame.MOUSEMOTION :

            mousex , mousey = event.pos

        if event.type == pygame.MOUSEBUTTONUP and active == 1 :

            if mousex >= 450 and mousex <= 550 and mousey >= 250 and mousey <= 350 :
                
                submarine_health = 230

                gun_img = pygame.image.load("game_gun1.png")
                gun_img = pygame.transform.scale(gun_img , (gun_width//2 , gun_height//2))
                bullet_img1 = pygame.image.load("game_bullets.png")
                bullet_img2 = pygame.image.load("game_bullet.png")
                bullet_img3 = pygame.image.load("game_bulletss.png")
                bullet_img4 = pygame.image.load("game_bullets.png")
                bullet_img5 = pygame.image.load("game_bullet.png")
                bullet_img6 = pygame.image.load("game_bulletss.png")
                bullet_img7 = pygame.image.load("game_bullets.png")
                
                submarinex = 100
                score_last = 0
                EF = 0
                activate = -1
                grenade_code = -1
                gunx1 = 900
                gunx2 = 900
                gunx3 = 900
                gunx4 = 900
                gunx5 = 900
                gunx6 = 900
                gunx7 = 900
                bulletx1 = 804
                bulletx2 = 804
                bulletx3 = 804
                bulletx4 = 804
                bulletx5 = 804
                bulletx6 = 804
                bulletx7 = 804
                grenade_state = "reserve"
                active = -1                
           
    if activate != -1 :
        
        EF = CD - AB
        CF = times/1000 - EF
        EF = CF
        
    submarinex += submarinexch
    submariney += submarineych
    
    if submarinex >= 583 :
        submarinexch = 0

    if submarinex <= 10:
        submarinexch = 0

    if submariney <= 5 :
        submarineych = 0

    if submariney >= 440:
        submarineych = 0

    for i in range(0,tiles):
                
        screen.blit(background, (i*1000 + scroll , 0))
    scroll -= 2
    
    if abs(scroll) > 1000 :
        scroll = 0

    # BULLET RESEARCH - AUTOMATIC AI RANDOM BULLET SHOOTER
        
    screen.blit(gun_img , (gunx1,guny1))
    screen.blit(gun_img , (gunx2 , guny2))
    screen.blit(gun_img , (gunx3 , guny3))
    screen.blit(submarine, (submarinex,submariney))
    screen.blit(gun_img , (gunx4,guny4))
    screen.blit(gun_img , (gunx5,guny5))
    screen.blit(gun_img , (gunx6 , guny6))
    screen.blit(gun_img , (gunx7 , guny7))

    if activate == 1 and bullet1_state == "Fire":
        screen.blit(bullet_img1 , (bulletx1 , bullety1))
    if activate == 1 and bullet3_state == "Fire" :
        screen.blit(bullet_img3 , (bulletx3 , bullety3))
    if activate == 1 and bullet5_state == "Fire" :
        screen.blit(bullet_img5 , (bulletx5 , bullety5))
        
    if activate == 2 and bullet2_state == "Fire":
        screen.blit(bullet_img2 , (bulletx2 , bullety2))
    if activate == 2 and bullet3_state == "Fire" :
        screen.blit(bullet_img3 , (bulletx3 , bullety3))
    if activate == 2 and bullet4_state == "Fire" :
        screen.blit(bullet_img4 , (bulletx4 , bullety4))
    
    if activate == 0 or activate == 3 and bullet3_state == "Fire":
        screen.blit(bullet_img3 , (bulletx3 , bullety3))
        
    if activate == 4 and bullet4_state == "Fire":
        screen.blit(bullet_img4 , (bulletx4 , bullety4))
    if activate == 4 and bullet5_state == "Fire" :
        screen.blit(bullet_img5 , (bulletx5 , bullety5))
    if activate == 4 and bullet7_state == "Fire" :
        screen.blit(bullet_img7 , (bulletx7 , bullety7))

    if activate == 5 and bullet5_state == "Fire": 
        screen.blit(bullet_img5 , (bulletx5 , bullety5))
    if activate == 5 and bullet1_state == "Fire" :
        screen.blit(bullet_img1 , (bulletx1 , bullety1))
    if activate == 5 and bullet2_state == "Fire" :
        screen.blit(bullet_img2 , (bulletx2 , bullety2))
        
    if activate == 6 and bullet6_state == "Fire":
        screen.blit(bullet_img6 , (bulletx6 , bullety6))
    if activate == 6 and bullet3_state == "Fire" :
        screen.blit(bullet_img3 , (bulletx3 , bullety3))
    if activate == 6 and bullet1_state == "Fire" :
        screen.blit(bullet_img1 , (bulletx1 , bullety1))
        
    if activate == 7 and bullet7_state == "Fire":
        screen.blit(bullet_img7 , (bulletx7 , bullety7))
    if activate == 7 and bullet3_state == "Fire" :
        screen.blit(bullet_img3 , (bulletx3 , bullety3))
    if activate == 7 and bullet2_state == "Fire" :
        screen.blit(bullet_img2 , (bulletx2 , bullety2))
        
    if int(EF) > 0 and int(EF) <= 60:    
        bulletx1 -= 9
        bulletx2 -= 8
        bulletx3 -= 8
        bulletx4 -= 8
        bulletx5 -= 8
        bulletx6 -= 8
        bulletx7 -= 11
        
    if int(EF) > 60 and int(EF) <= 120 :
        bulletx1 -= 11
        bulletx2 -= 13
        bulletx3 -= 13
        bulletx4 -= 14
        bulletx5 -= 15
        bulletx6 -= 12
        bulletx7 -= 10

    if int(EF) > 120 and int(EF) <= 180 :
        bulletx1 -= 11
        bulletx2 -= 13
        bulletx3 -= 13
        bulletx4 -= 14
        bulletx5 -= 15
        bulletx6 -= 12
        bulletx7 -= 10
        
    if int(EF) > 180 and int(EF) <= 300:
        bulletx1 -= 11
        bulletx2 -= 14
        bulletx3 -= 14
        bulletx4 -= 15
        bulletx5 -= 16
        bulletx6 -= 13
        bulletx7 -= 10

    if int(EF) > 300 and int(EF) <= 500 :

        bulletx1 -= 11
        bulletx2 -= 14
        bulletx3 -= 14
        bulletx4 -= 15
        bulletx5 -= 16
        bulletx6 -= 13
        bulletx7 -= 10

    if int(EF) > 500 and int(EF) <= 700 :

        bulletx1 -= 11
        bulletx2 -= 15
        bulletx3 -= 15
        bulletx4 -= 16
        bulletx5 -= 17
        bulletx6 -= 13
        bulletx7 -= 10

    if int(EF) > 700 :

        bulletx1 -= 11
        bulletx2 -= 17
        bulletx3 -= 17
        bulletx4 -= 17
        bulletx5 -= 17
        bulletx6 -= 17
        bulletx7 -= 10          

    offset1 = (submarinex - bulletx1 , submariney - bullety1)
    offset2 = (submarinex - bulletx2 , submariney - bullety2)
    offset3 = (submarinex - bulletx3 , submariney - bullety3)
    offset4 = (submarinex - bulletx4 , submariney - bullety4)
    offset5 = (submarinex - bulletx5 , submariney - bullety5)
    offset6 = (submarinex - bulletx6 , submariney - bullety6)
    offset7 = (submarinex - bulletx7 , submariney - bullety7)
    
    result1 = bullet_mask1.overlap(submarine_mask , offset1)
    result2 = bullet_mask2.overlap(submarine_mask , offset2)
    result3 = bullet_mask3.overlap(submarine_mask , offset3)
    result4 = bullet_mask4.overlap(submarine_mask , offset4)
    result5 = bullet_mask5.overlap(submarine_mask , offset5)
    result6 = bullet_mask6.overlap(submarine_mask , offset6)
    result7 = bullet_mask7.overlap(submarine_mask , offset7)

    if result1 :
        bulletx1 = -200
        bullet1_state == "Reserve"
        submarine_health -= 15
        
    if result2 :
        bulletx2 = -200
        bullet2_state == "Reserve"
        submarine_health -= 15
        
    if result3 :
        bulletx3 = -200
        bullet3_state == "Reserve"
        submarine_health -= 15
        
    if result4 :
        bulletx4 = -200
        bullet4_state == "Reserve"
        submarine_health -= 15
        
    if result5 :
        bulletx5 = -200
        bullet5_state == "Reserve"
        submarine_health -= 15
        
    if result6 :
        bulletx6 = -200
        bullet6_state == "Reserve"
        submarine_health -= 15
                
    if result7 :
        bulletx7 = -200
        bullet7_state == "Reserve"
        submarine_health -= 15
        
    if bulletx1 <= 0 :
        bullet1_state = "Reserve"
        
    if bulletx2 <= 0 :
        bullet2_state = "Reserve"
        
    if bulletx3 <= 0 :
        bullet3_state = "Reserve"
        
    if bulletx4 <= 0 :
        bullet4_state = "Reserve"
        
    if bulletx5 <= 0 :
        bullet5_state = "Reserve"
        
    if bulletx6 <= 0 :
        bullet6_state = "Reserve"
        
    if bulletx7 <= 0 :
        bullet7_state = "Reserve"
        
    if bullet1_state == "Reserve" and bullet2_state == "Reserve" and bullet3_state == "Reserve" and bullet4_state == "Reserve" and bullet5_state == "Reserve" and bullet6_state == "Reserve" and bullet7_state == "Reserve" and activate != -1:
            
        random_no()
        
        activate = random_nos
        
        if activate == 1 :
            bulletx1 = 804
            bulletx3 = 804
            bulletx5 = 804
            bullet1_state = "Fire"
            bullet5_state = "Fire"
            bullet3_state = "Fire"
            
        if activate == 2 :
            bulletx2 = 804
            bulletx3 = 804
            bulletx4 = 804
            bullet2_state = "Fire"
            bullet3_state = "Fire"
            bullet4_state = "Fire"
            
        if activate == 3 or activate == 0:
            bulletx3 = 804
            bullet3_state = "Fire"
            
        if activate == 4 :
            bulletx4 = 804
            bulletx5 = 804
            bulletx7 = 804
            bullet4_state = "Fire"
            bullet5_state = "Fire"
            bullet7_state = "Fire"
            
        if activate == 5 :
            bulletx1 = 804
            bulletx2 = 804
            bulletx5 = 804
            bullet5_state = "Fire"
            bullet1_state = "Fire"
            bullet2_state = "Fire"
            
        if activate == 6 :
            bulletx1 = 804
            bulletx3 = 804
            bulletx6 = 804
            bullet6_state = "Fire"
            bullet3_state = "Fire"
            bullet1_state = "Fire"
            
        if activate == 7 :
            bulletx2 = 804
            bulletx3 = 804
            bulletx7 = 804
            bullet7_state = "Fire"
            bullet3_state = "Fire"
            bullet2_state = "Fire"
                    
    # GRENADE RESEARCH - AUTOMATIC AI GRENADE LAUCHER

    if int(EF) == 120 and grenade_code == -1:
        grenade_activator()
        grenade_activation = grenade_code
        grenadex = 300
    
    if grenadey >= 600 - 57 and grenade_code != -1:
        grenadey = -100
        grenade_state = "reserve"
        grenade_activator()
        grenade_activation = grenade_code
        grenade_identifier = -1
    
    if grenade_activation != -1 and grenade_state == "reserve" :
        grenade_state = "fire"

    if grenade_code == 1 :
        grenadex = 60
    if grenade_code == 2 :
        grenadex = 300
    if grenade_code == 3 :
        grenadex = 400
 
    if grenade_state == "fire" :
        screen.blit(grenade_img , (grenadex , grenadey))

        if int(EF) < 600 :
            grenadey += 2

        if int(EF) > 600 :
            grenadey += 3
        
    grenade_offset = (submarinex - grenadex , submariney - grenadey)
    grenade_result = grenade_mask.overlap(submarine_mask , grenade_offset)

    if grenade_result and grenade_code != -1 :
        
        explosionx = grenadex
        explosiony = grenadey
        screen.blit(explosion , (explosionx , explosiony))
        grenade_state = "reserve"
        grenadey = -100
        grenade_activator()
        grenade_activation = grenade_code
        grenade_identifier = 1
        submarine_health -= 30
            
    if grenadey > -80 and grenadey < -20 :
        screen.blit(danger_sign , (grenadex , 20))

    if grenade_identifier == 1 and grenadey < -60:
        screen.blit(explosion , (explosionx , explosiony))

    pygame.draw.rect(screen , (255,0,0) , (10,10,200,10))
    pygame.draw.rect(screen , (80,120,100) , (10,10,submarine_health , 10))

    pygame.draw.rect(screen , (255 , 0, 0) , (400,10,100,10))
    pygame.draw.rect(screen , (80,100,120) , (400,10,submarine_fuel , 10))

    if int(EF) % 30 == 0 and int(EF) >= 20:

        powerupx = 1100
        powerupxch = -3

    powerupx += powerupxch

    screen.blit(power_up , (powerupx , powerupy))

    power_up_offset = (submarinex - powerupx , submariney - powerupy)

    power_up_result = power_up_mask.overlap(submarine_mask , power_up_offset)

    if power_up_result :
        submarine_input_past = submarine_input
        powerupxch = 0
        powerupx = 10000
        submarine_input = submarine_generator()
        
        if submarine_input == submarine_input_past and submarine_input != 5:
            submarine_input += 1
        if submarine_input == submarine_input_past and submarine_input == 5 :
            submarine_input -= 1
        
        if submarine_health >= 175 :
            submarine_health += 200 - submarine_health
        if submarine_health < 175 :
            submarine_health += 25
            
        bg_generating_machine()

        bg_code = bg_generator

        if bg_code == 1 :
            background = pygame.image.load("underwater.jpg")
            background = pygame.transform.scale(background , (2000,1200))
        if bg_code == 2 :
            background = pygame.image.load("underwater1.jpg")
            background = pygame.transform.scale(background , (2000,1200))
        if bg_code == 3 :
            background = pygame.image.load("underwater2.jpg")
            background = pygame.transform.scale(background , (2000,1200))
        if bg_code == 4 :
            background = pygame.image.load("underwater3.jpg")
            background = pygame.transform.scale(background , (2000,1200))

    if submarine_input == 1:
        submarine = pygame.image.load("submarine.png")
    if submarine_input == 2:
        submarine = pygame.image.load("MARINE.png")
    if submarine_input == 3:
        submarine = pygame.image.load("submarine1.png")
    if submarine_input == 4:
        submarine = pygame.image.load("submarine2.png")
    if submarine_input == 5:
        submarine = pygame.image.load("submarine3.png")

    if int(EF) % 43 == 0 and int(EF) > 20 :

        fuelx = 1100
        fuelxch = -3

    fuelx += fuelxch

    screen.blit(fuel , (fuelx , fuely))

    fuel_offset = (submarinex - fuelx , submariney - fuely)

    fuel_result = fuel_mask.overlap(submarine_mask , fuel_offset)

    if fuel_result :

        fuelx = 10000
        fuelxch = 0
        if submarine_fuel <= 50 :
            submarine_fuel += 50
        if submarine_fuel > 50 :
            submarine_fuel += 100 - submarine_fuel

    if active == 1 :

        submarinex = 10000
        gunx1 = 10000
        gunx2 = 10000
        gunx3 = 10000
        gunx4 = 10000
        gunx5 = 10000
        gunx6 = 10000
        gunx7 = 10000

        bulletx1 = 10000
        bulletx2 = 10000
        bulletx3 = 10000
        bulletx4 = 10000
        bulletx5 = 10000
        bulletx6 = 10000
        bulletx7 = 10000
        grenadex = 10000

    if submarine_health <= 0 and active == -1 :
        score_last = int(EF)
        print(score_last)
        
        active = 1
    
    if submarine_health > 0 :     
        writing_font()

    if submarine_health <= 0 :
        writing_font1()
        screen.blit(retry , (450,250))

    if int(EF) > 400 :

            gun_img = pygame.image.load("gunspl1.png")
            if bulletx1 <= 0 :
                bullet_img1 = pygame.image.load("nuclear_bomb.png")
            if bulletx2 <= 0 :
                bullet_img2 = pygame.image.load("nuclear_bomb.png")
            if bulletx3 <= 0 :
                bullet_img3 = pygame.image.load("nuclear_bomb.png")
            if bulletx4 <= 0 :
                bullet_img4 = pygame.image.load("nuclear_bomb.png")
            if bulletx5 <= 0 :
                bullet_img5 = pygame.image.load("nuclear_bomb.png")
            if bulletx6 <= 0 :
                bullet_img6 = pygame.image.load("nuclear_bomb.png")
            if bulletx7 <= 0 :
                bullet_img7 = pygame.image.load("nuclear_bomb.png")

    if int(EF) != 0 and int(EF) % 4 == 0 and fuel_monitor == 0:
        submarine_fuel -= 4
        fuel_monitor = 1
    if int(EF) % 4 != 0 :
        fuel_monitor = 0

    if submarine_fuel <= 0 :
        submarine_health = 0 
    
    pygame.display.update()

pygame.quit()
