import pygame
from pygame.draw import *
from random import randint

pygame.init()

RED = (255, 0, 0)
YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)

screen = pygame.display.set_mode((1300, 900))

FPS = 70


class Player_unit:
    def __init__(self) -> None:
        self.shag_unit = 5
        self.start_pos_unit_x = randint(100, 1100)
        self.start_pos_unit_y = randint(450, 700)
        self.radius = randint(10, 20)
        self.color = YELLOW

    def animation_unit(self):
        if plus:
            self.start_pos_unit_x += self.shag_unit
        elif not plus:
            self.start_pos_unit_x -= self.shag_unit
            if self.start_pos_unit_x + self.radius <= 0:
                self.start_pos_unit_x= self.radius
            elif self.start_pos_unit_x + self.radius >= 1200:
                self.start_pos_unit_x = 1200 - 2*self.radius

    def unit(self):
        circle(screen, self.color, (self.start_pos_unit_x, self.start_pos_unit_y), self.radius, 0)


class Wall:
    def __init__(self) -> None:
        self.position_wall_x = randint(0, 1200)
        self.position_wall_y = randint(0, 200)
        self.size_wall_x = randint(100, 600)
        self.size_wall_y = randint(10, 20)
        self.color = RED
        self.wall_speed = 5
        self.Call_member_wall = Call_member_wall
        self.points  = 0
        
    
    def moowe_wall(self):
        global Call_member_wall
        if self.position_wall_y <= 900:
            self.position_wall_y += self.wall_speed
        elif self.position_wall_y >= 900:
            Call_member_wall = True
            return
    
    def wall_obg(self):
        rect(screen, self.color, (self.position_wall_x, self.position_wall_y, self.size_wall_x, self.size_wall_y), 0)
    
    def point(self, radius_unit, pos_unit_x, pos_unit_y):
        self.place_x = radius_unit + pos_unit_x
        if (self.place_x > self.position_wall_x + self.size_wall_x or\
             self.place_x < self.position_wall_x) and\
            self.position_wall_y - pos_unit_y >= self.wall_speed:
            self.points += 10
            line(screen, YELLOW, (1000, 100), (1000, 150), 7)
        else:
            line(screen, RED, (1000, 100), (1000, 150), 7)

clock = pygame.time.Clock()
screen.fill(BLACK)
Finish = False
Call_member_unit = True
Call_member_wall = True
pygame.display.update()

while not Finish:
    clock.tick(FPS)
    if Call_member_wall:
            A = Wall()
            B = Wall()
            Call_member_wall = False
    if Call_member_unit:
            C = Player_unit()
            Call_member_unit = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Finish = True
        if event.type == pygame.KEYDOWN:
            plus = True
        elif pygame.KEYUP:
            plus = False
    A.wall_obg()
    B.wall_obg()
    A.moowe_wall()
    B.moowe_wall()
    A.point(C.start_pos_unit_x, C.radius, C.start_pos_unit_y)
    C.unit()
    C.animation_unit()
    pygame.display.update()
    screen.fill(BLACK)
    #print(C.start_pos_unit_x, A.position_wall_x, A.position_wall_x + A.size_wall_x)
    print(A.points)
pygame.quit()