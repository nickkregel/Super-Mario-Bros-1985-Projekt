import pygame
from sys import exit
import sys
import os

class Block1:
    def __init__(self, image, position):
        self.default_image = image
        self.hit_image = Block2_surface
        self.image = self.default_image
        self.position = position
        self.rect = self.image.get_rect(topleft=position)
        self.hit = False
        self.show_coin_timer = 0

    def update_rect(self, scroll_offset):
        self.rect.topleft = (self.position[0] + scroll_offset, self.position[1])
        return self.rect

    def check_collision(self, player_rect, player_gravity):
        global coin_count

        on_ground = False
        if player_rect.colliderect(self.rect):
            if player_rect.bottom <= self.rect.top + 20 and player_gravity >= 0:
                player_rect.bottom = self.rect.top
                player_gravity = 0
                on_ground = True
            elif player_rect.top >= self.rect.bottom - 20 and player_gravity < 0:
                player_rect.top = self.rect.bottom
                player_gravity = 1
                if not self.hit:
                    self.image = self.hit_image
                    self.hit = True
                    coin_count += 1
                    self.show_coin_timer = 45 
            elif player_rect.right >= self.rect.left and player_rect.left < self.rect.left:
                player_rect.right = self.rect.left
            elif player_rect.left <= self.rect.right and player_rect.right > self.rect.right:
                player_rect.left = self.rect.right
        return player_rect, player_gravity, on_ground

    def draw(self, surface, scroll_offset):
        surface.blit(self.image, (self.position[0] + scroll_offset, self.position[1]))

        
        if self.show_coin_timer > 0:
            coin_pos = (self.position[0] + scroll_offset + (self.rect.width - 50) // 2,
                        self.position[1] - 80)
            surface.blit(coin_big_surface, coin_pos)
            self.show_coin_timer -= 1


class Block3:
    def __init__(self, image, position):
        self.image = image
        self.position = position
        self.rect = self.image.get_rect(topleft=position)

    def update_rect(self, scroll_offset):
        self.rect.topleft = (self.position[0] + scroll_offset, self.position[1])
        return self.rect

    def check_collision(self, player_rect, player_gravity):
        on_ground = False
        if player_rect.colliderect(self.rect):
            if player_rect.bottom <= self.rect.top + 20 and player_gravity >= 0:
                player_rect.bottom = self.rect.top
                player_gravity = 0
                on_ground = True
            elif player_rect.top >= self.rect.bottom - 20 and player_gravity < 0:
                player_rect.top = self.rect.bottom
                player_gravity = 1
            elif player_rect.right >= self.rect.left and player_rect.left < self.rect.left:
                player_rect.right = self.rect.left
            elif player_rect.left <= self.rect.right and player_rect.right > self.rect.right:
                player_rect.left = self.rect.right
        return player_rect, player_gravity, on_ground

    def draw(self, surface, scroll_offset):
        surface.blit(self.image, (self.position[0] + scroll_offset, self.position[1]))

class Block4:
    def __init__(self, image, position):
        self.image = image
        self.position = position
        self.rect = self.image.get_rect(topleft=position)

    def update_rect(self, scroll_offset):
        self.rect.topleft = (self.position[0] + scroll_offset, self.position[1])
        return self.rect

    def check_collision(self, player_rect, player_gravity):
        on_ground = False
        if player_rect.colliderect(self.rect):
            if player_rect.bottom <= self.rect.top + 20 and player_gravity >= 0:
                player_rect.bottom = self.rect.top
                player_gravity = 0
                on_ground = True
            elif player_rect.top >= self.rect.bottom - 20 and player_gravity < 0:
                player_rect.top = self.rect.bottom
                player_gravity = 1
            elif player_rect.right >= self.rect.left and player_rect.left < self.rect.left:
                player_rect.right = self.rect.left
            elif player_rect.left <= self.rect.right and player_rect.right > self.rect.right:
                player_rect.left = self.rect.right
        return player_rect, player_gravity, on_ground

    def draw(self, surface, scroll_offset):
        surface.blit(self.image, (self.position[0] + scroll_offset, self.position[1]))

class Pipe:
    def __init__(self, image, position):
        self.image = image
        self.position = position
        self.rect = self.image.get_rect(topleft=position)

    def update_rect(self, scroll_offset):
        self.rect.topleft = (self.position[0] + scroll_offset, self.position[1])
        return self.rect

    def check_collision(self, player_rect, player_gravity):
        on_ground = False
        if player_rect.colliderect(self.rect):
            if player_rect.bottom <= self.rect.top + 20 and player_gravity >= 0:
                player_rect.bottom = self.rect.top
                player_gravity = 0
                on_ground = True
            elif player_rect.top >= self.rect.bottom - 20 and player_gravity < 0:
                player_rect.top = self.rect.bottom
                player_gravity = 1
            elif player_rect.right >= self.rect.left and player_rect.left < self.rect.left:
                player_rect.right = self.rect.left
            elif player_rect.left <= self.rect.right and player_rect.right > self.rect.right:
                player_rect.left = self.rect.right
        return player_rect, player_gravity, on_ground

    def draw(self, surface, scroll_offset):
        surface.blit(self.image, (self.position[0] + scroll_offset, self.position[1]))

class Goomba:
    def __init__(self, image, position):
        self.image = image
        self.position = list(position)
        self.rect = self.image.get_rect(topleft=position)
        self.speed = -1 

    def update(self):
        self.position[0] += self.speed
        self.rect.topleft = (self.position[0], self.position[1])

    def update_rect(self, scroll_offset):
        self.rect.topleft = (self.position[0] + scroll_offset, self.position[1])
        return self.rect

    def check_collision(self, player_rect, player_gravity):
        on_ground = False
        if player_rect.colliderect(self.rect):
            if player_rect.bottom <= self.rect.top + 20 and player_gravity >= 0:
                player_rect.bottom = self.rect.top
                player_gravity = 0
                on_ground = True
            elif player_rect.top >= self.rect.bottom - 20 and player_gravity < 0:
                player_rect.top = self.rect.bottom
                player_gravity = 1
            elif player_rect.right >= self.rect.left and player_rect.left < self.rect.left:
                player_rect.right = self.rect.left
            elif player_rect.left <= self.rect.right and player_rect.right > self.rect.right:
                player_rect.left = self.rect.right
        return player_rect, player_gravity, on_ground

    def draw(self, surface, scroll_offset):
        surface.blit(self.image, (self.position[0] + scroll_offset, self.position[1]))

class Ground:
    def __init__(self, image, position):
        self.image = image
        self.position = position
        self.rect = self.image.get_rect(topleft=position)

    def update_rect(self, scroll_offset):
        self.rect.topleft = (self.position[0] + scroll_offset, self.position[1])
        return self.rect

    def check_collision(self, player_rect, player_gravity):
        on_ground = False
        if player_rect.colliderect(self.rect):
            if player_rect.bottom <= self.rect.top + 20 and player_gravity >= 0:
                player_rect.bottom = self.rect.top
                player_gravity = 0
                on_ground = True
            elif player_rect.top >= self.rect.bottom - 20 and player_gravity < 0:
                player_rect.top = self.rect.bottom
                player_gravity = 1
            elif player_rect.right >= self.rect.left and player_rect.left < self.rect.left:
                player_rect.right = self.rect.left
            elif player_rect.left <= self.rect.right and player_rect.right > self.rect.right:
                player_rect.left = self.rect.right
        return player_rect, player_gravity, on_ground

    def draw(self, surface, scroll_offset):
        surface.blit(self.image, (self.position[0] + scroll_offset, self.position[1]))

def player_animation():
    global player_surface, player_index, is_jumping, last_direction, direction
    if is_jumping:
        player_surface = player_jump_right if last_direction == 1 else player_jump_left
    elif direction != 0:
        player_index += 0.1
        if player_index >= len(player_walk_right):
            player_index = 0
        player_surface = player_walk_right[int(player_index)] if last_direction == 1 else player_walk_left[int(player_index)]
    else:
        player_surface = player_walk_right[0] if last_direction == 1 else player_walk_left[0]

def player_hit(player_rect, goomba_rect, player_gravity):
    
    if player_rect.colliderect(goomba_rect):
        if not (player_rect.bottom <= goomba_rect.top + 20 and player_gravity >= 0):
            pygame.quit()
            sys.exit()
    return

pygame.init()
screen = pygame.display.set_mode((1000, 600))
pygame.display.set_caption("Mario Bros 1985")
clock = pygame.time.Clock()

bg_surface = pygame.image.load('images/bg.jpg')
bg_surface = pygame.transform.scale(bg_surface, (15000, 600))

ground_surface = pygame.image.load('images/ground.png')
ground_surface = pygame.transform.scale(ground_surface, (800, 100))

Block1_surface = pygame.image.load('images/Block1.png')
Block1_surface = pygame.transform.scale(Block1_surface, (75, 75))
Block2_surface = pygame.image.load('images/Block2.png')
Block2_surface = pygame.transform.scale(Block2_surface, (75, 75))

block3_surface = pygame.image.load('images/Block3.png')
block3_surface = pygame.transform.scale(block3_surface, (75, 75))

Block4_surface = pygame.image.load('images/Block4.png')
Block4_surface = pygame.transform.scale(Block4_surface, (75, 75))

pipe_surface = pygame.image.load('images/pipe.png')
pipe_surface = pygame.transform.scale(pipe_surface, (100, 150))

goomba_surface = pygame.image.load('images/goomba1.png')
goomba_surface = pygame.transform.scale(goomba_surface, (75, 75))

player_walk1 = pygame.image.load('images/mario.png')
player_walk2 = pygame.image.load('images/mario2.png')
player_walk3 = pygame.image.load('images/mario3.png')
player_walk4 = pygame.image.load('images/mario4.png')

coin_surface = pygame.image.load('images/coin.png')
coin_surface = pygame.transform.scale(coin_surface, (25, 25))
coin_font = pygame.font.SysFont(None, 40)
coin_count = 0
coin_big_surface = pygame.transform.scale(coin_surface, (50, 50))

flag_img = pygame.image.load("images/Flagpole.png").convert_alpha()
flag_img = pygame.transform.scale(pygame.image.load("images/Flagpole.png"), (475, 475))
flag_rect = flag_img.get_rect(topleft=(13200, 50))
flag_touched = False
level_completed = False

player_walk_right = [player_walk1, player_walk2, player_walk3, player_walk4]
player_walk_left = [pygame.transform.flip(img, True, False) for img in player_walk_right]
player_jump_right = pygame.image.load('images/mario_jump.png')
player_jump_left = pygame.transform.flip(player_jump_right, True, False)

player_index = 0
player_surface = player_walk_right[player_index]
player_rect = player_surface.get_rect(topleft=(80, 445))

player_gravity = 0
is_jumping = False
last_direction = 1
direction = 0

speed = 0
acceleration = 0.25
max_speed = 10

scroll_offset = 0

block1_positions = [
    (800, 275),
    (1275, 275),
    (1350, 50),
    (1425, 275),
    (4075, 275),
    (5650, 50),
    (6400, 275),
    (6625, 275),
    (6625, 50),
    (6850, 275),
    (8275, 50),
    (8350, 50),
    (11625, 275)
]
block3_positions = [
    (1200, 275),
    (1350, 275),
    (1500, 275),
    (4000, 275),
    (4150, 275),
    (4225, 50),
    (4300, 50),
    (4375, 50),
    (4450, 50),
    (4525, 50),
    (4600, 50),
    (4675, 50),
    (4750, 50),
    (4825, 50),
    (4900, 50),
    (4975, 50),
    (5350, 50),
    (5425, 50),
    (5500, 50),
    (5575, 50),
    (5650, 275),
    (6025, 275),
    (6100, 275),
    (7225, 275),
    (7375, 50),
    (7450, 50),
    (7525, 50),
    (7600, 50),
    (8200, 50),
    (8275, 275),
    (8350, 275),
    (8425, 50),
    (11475, 275),
    (11550, 275),
    (11700, 275)

]
block4_positions = [
    (8725, 450),
    (8800, 450),
    (8800, 375),
    (8875, 450),
    (8875, 375),
    (8875, 300),
    (9175, 300),
    (9175, 375),
    (9175, 450),
    (9250, 375),
    (9250, 450),
    (9325, 450),
    (9925, 450),
    (10000, 450),
    (10000, 375),
    (10075, 450),
    (10075, 375),
    (10075, 300),
    (10150, 450),
    (10150, 375),
    (10150, 300),
    (10375, 300),
    (10375, 375),
    (10375, 450),
    (10450, 375),
    (10450, 450),
    (10525, 450),
    (12500, 450),
    (12575, 450),
    (12575, 375),
    (12650, 450),
    (12650, 375),
    (12650, 300),
    (12725, 450),
    (12725, 375),
    (12725, 300),
    (12725, 225),
    (12800, 450),
    (12800, 375),
    (12800, 300),
    (12800, 225),
    (12800, 150),
    (12875, 450),
    (12875, 375),
    (12875, 300),
    (12875, 225),
    (12875, 150)
]
pipe_positions = [
    (1800, 450),
    (2500, 400),
    (3200, 375),
    (11025, 450),
    (12400, 450)
]
ground_positions = [
    (0, 525),
    (800, 525),
    (1600, 525),
    (2400, 525),
    (3200, 525),
    (4000, 525),
    (4800, 525),
    (5600, 525),
    (6400, 525),
    (7200, 525),
    (8000, 525),
    (8800, 525),
    (9600, 525),
    (10400, 525),
    (11200, 525),
    (12000, 525),
    (12800, 525),
    (13600, 525),
    (14400, 525),
    (15200, 525)
]
goomba_positions = [
    (600, 450),
    (3100, 450),
    (2950, 450)
]

blocks1 = [Block1(Block1_surface, pos) for pos in block1_positions]
blocks3 = [Block3(block3_surface, pos) for pos in block3_positions]
blocks4 = [Block4(Block4_surface, pos) for pos in block4_positions]
pipes = [Pipe(pipe_surface, pos) for pos in pipe_positions]
grounds = [Ground(ground_surface, pos) for pos in ground_positions]
goombas = [Goomba(goomba_surface, pos) for pos in goomba_positions]

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
            pygame.quit()
            sys.exit()

        if event.key == pygame.K_r:
            pygame.quit()
            os.execl(sys.executable, sys.executable, *sys.argv)

    keys = pygame.key.get_pressed()
    on_ground = False

    for ground in grounds:
        ground.update_rect(scroll_offset)
        player_rect, player_gravity, ground_on_ground = ground.check_collision(player_rect, player_gravity)
        if ground_on_ground:
            on_ground = True

    for block in blocks1:
        block.update_rect(scroll_offset)
        player_rect, player_gravity, block_on_ground = block.check_collision(player_rect, player_gravity)
        if block_on_ground:
            on_ground = True

    for block in blocks3:
        block.update_rect(scroll_offset)
        player_rect, player_gravity, block_on_ground = block.check_collision(player_rect, player_gravity)
        if block_on_ground:
            on_ground = True

    for block in blocks4:
        block.update_rect(scroll_offset)
        player_rect, player_gravity, block_on_ground = block.check_collision(player_rect, player_gravity)
        if block_on_ground:
            on_ground = True

    for pipe in pipes:
        pipe.update_rect(scroll_offset)
        player_rect, player_gravity, pipe_on_ground = pipe.check_collision(player_rect, player_gravity)
        if pipe_on_ground:
            on_ground = True

    for pipe in goombas:
        pipe.update_rect(scroll_offset)
        player_rect, player_gravity, pipe_on_ground = pipe.check_collision(player_rect, player_gravity)
        if pipe_on_ground:
            on_ground = True

    if on_ground:
        is_jumping = False

    if player_rect.bottom >= 525:
        player_rect.bottom = 525
        player_gravity = 0
        on_ground = True
        is_jumping = False

    if keys[pygame.K_SPACE] and on_ground:
        player_gravity = -28
        is_jumping = True

    if keys[pygame.K_d]:
        direction = 1
    elif keys[pygame.K_a]:
        direction = -1
    else:
        direction = 0

    if direction != 0:
        last_direction = direction

    speed = min(speed + acceleration, max_speed) if direction != 0 else 0

    if direction == 1:
        if player_rect.centerx < 500:
            player_rect.x += speed
        else:
            scroll_offset -= speed
    elif direction == -1:
        if scroll_offset < 0 and player_rect.centerx <= 500:
            scroll_offset += speed
        elif player_rect.x > 0:
            player_rect.x -= speed

    player_gravity += 1
    player_rect.y += player_gravity

    
    flag_screen_x = flag_rect.x + scroll_offset
    if player_rect.colliderect(pygame.Rect(flag_screen_x, flag_rect.y, flag_rect.width, flag_rect.height)) and not level_completed:
        flag_touched = True
        level_completed = True


    if flag_touched:
        player_gravity = 1
        direction = 0
        if player_rect.bottom < 525:
         player_rect.y += player_gravity
        else:
        
            screen.fill((0, 0, 0))
            font = pygame.font.SysFont(None, 100)
            text = font.render("Level Abgeschlossen", True, (255, 255, 255))
            rect = text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2))
            screen.blit(text, rect)
            pygame.display.update()
            pygame.time.wait(3000)
            exit()


    player_animation()

    screen.fill((0, 0, 0))
    screen.blit(bg_surface, (scroll_offset, 0))
    screen.blit(bg_surface, (1000 + scroll_offset, 0))

    coin_text = coin_font.render(f"x {coin_count:02}", True, (255, 255, 255))
    coin_x = screen.get_width() // 2 - (coin_surface.get_width() + coin_text.get_width()) // 2
    screen.blit(coin_surface, (coin_x, 10))
    screen.blit(coin_text, (coin_x + coin_surface.get_width() + 5, 10))

    for ground in grounds:
        ground.draw(screen, scroll_offset)

    for pipe in pipes:
        pipe.draw(screen, scroll_offset)

    for block in blocks1:
        block.draw(screen, scroll_offset)

    for block in blocks3:
        block.draw(screen, scroll_offset)

    for block in blocks4:
        block.draw(screen, scroll_offset)

    for goomba in goombas:
        goomba.update()
        goomba.draw(screen, scroll_offset)


    screen.blit(player_surface, player_rect)
    screen.blit(flag_img, (flag_rect.x + scroll_offset, flag_rect.y))

    pygame.display.update()
    clock.tick(60)


















