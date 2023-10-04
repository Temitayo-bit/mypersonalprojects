import pygame, sys,random


pygame.init()

def ball_center():
    global ball_speed_2, ball_speed_1, player_score, opponent_score, timer
    current = pygame.time.get_ticks()
    ball.center = (width/2, height/2)

    if current - timer < 700:
        number_1 = font.render("3", False, color1)
        screen.blit(number_1,(width/2 - 10, height/2 + 20))

    if 700 > current - timer < 1400:
        number_2 = font.render("2", False, color1)
        screen.blit(number_2,(width/2 - 10, height/2 + 20))

    if 1400 > current - timer < 2100:
        number_3 = font.render("1", False, color1)
        screen.blit(number_3,(width/2 - 10, height/2 + 20))

    

    if current - timer < 2100:
        ball_speed_1, ball_speed_2 = 0, 0
    else:
        ball_speed_2 = 7 * random.choice((1, -1))
        ball_speed_1 = 7 * random.choice((1, -1))
        timer = None

clock = pygame.time.Clock()
width = 1080
height = 650

screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("T's Ping pong")

ball = pygame.Rect(width/2 -15,height/2 - 15,30,30)
player = pygame.Rect(width - 20 , height/2 - 70,10 , 140)
opponent = pygame.Rect(10, height/2 - 70, 10, 140)

color1 = pygame.Color('white')
color2 = pygame.Color('black')

ball_speed_1 = 7 * random.choice ((1, -1))
ball_speed_2 = 7 * random.choice((1, -1))
player_move = 0
opponent_move = 7


player_score = 0
opponent_score = 0
font = pygame.font.Font("freesansbold.ttf", 28)


timer = True

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                player_move += 8
            if event.key == pygame.K_UP:
                player_move -=8

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                player_move += 8
            if event.key == pygame.K_DOWN:
                player_move -=8


    
    ball.x += ball_speed_1
    ball.y += ball_speed_2
    
    if ball.top <= 0 or ball.bottom >= height:
        ball_speed_2 *= -1
    if ball.left <= 0 :
        player_score +=1
        timer = pygame.time.get_ticks()
    
    if ball.right >= width:
        opponent_score += 1
        timer = pygame.time.get_ticks()

    if ball.colliderect(player) and ball_speed_1 > 0:
        if abs(ball.right - player.left) < 10:
            ball_speed_1 *= -1
        elif abs(ball.bottom - player.top) < 10 and ball_speed_2 > 0:
            ball_speed_2 *= -1
        elif abs(ball.top - player.bottom) <10 and ball_speed_2 < 0 :
            ball_speed_2 *= -1

    if ball.colliderect(opponent) and ball_speed_1 < 0:
        if abs(ball.left - opponent.right) < 10:
            ball_speed_1 *= -1
        elif abs(ball.bottom - opponent.top) < 10 and ball_speed_2 > 0:
            ball_speed_2 *= -1
        elif abs(ball.top - opponent.bottom) <10 and ball_speed_2 < 0:
            ball_speed_2 *= -1

    player.y += player_move
    if player.top <=0:
        player.top = 0
    if player.bottom >= height:
        player.bottom = height

    player.y += player_move
    if player.top <=0:
        player.top = 0
    if player.bottom >= height:
        player.bottom = height

    if opponent.top < ball.y:
        opponent.top += opponent_move
    if opponent.bottom > ball.y:
        opponent.bottom -= opponent_move




    screen.fill(color2)
    pygame.draw.rect(screen, color1, player)
    pygame.draw.rect(screen,color1, opponent)
    pygame.draw.ellipse(screen,color1, ball)
    pygame.draw.aaline(screen, color1, (width/2,0), (width/2, height))

    if timer:
        ball_center()

    player_side = font.render(f"{player_score}", False, color1)
    screen.blit(player_side, (570,325))
    opponent_side = font.render(f"{opponent_score}", False, color1)
    screen.blit(opponent_side, (500,325))

    pygame.display.flip()
    clock.tick(60)
