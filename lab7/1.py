import pygame
import math
import time
pygame.init()

screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

#images
main_clock  = pygame.transform.scale(pygame.image.load(r"lab7\mickey_images\clock.png"), (800, 600))
right_arm = pygame.image.load(r"lab7\mickey_images\rightarm.png")
left_arm = pygame.image.load(r"lab7\mickey_images\leftarm.png")

done = True

while done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = False

    #Displaying main clock
    screen.blit(main_clock, (0,0))

    #Current time
    current_time = time.localtime()
    minute = current_time.tm_min
    second = current_time.tm_sec

    #Angles
    minute_angle = minute * 6 + (second / 60) * 6   
    second_angle = second * 6 

    #Rotating
    rotated_minute = pygame.transform.rotate( pygame.transform.scale(right_arm, (800, 600)) , -minute_angle)
    new_rect = rotated_minute.get_rect(center=(400, 300))
    screen.blit(rotated_minute, new_rect)

    rotated_second = pygame.transform.rotate( pygame.transform.scale(left_arm, (40, 682)), -second_angle)
    ne_rect = rotated_second.get_rect(center=(400, 300))
    screen.blit(rotated_second, ne_rect)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
        