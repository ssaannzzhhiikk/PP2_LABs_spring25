import pygame
pygame.init()

# Data for usage
height = 400
width = 400
x, y = width // 2, height // 2
done = True
speed = 20
color = (255, 0, 0)
radius = 25

clock = pygame.time.Clock()
screen = pygame.display.set_mode((height, width))

while done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = False
                
        
        pressed = pygame.key.get_pressed()
        
        if pressed[pygame.K_UP] and y > radius + 1 :
               y -= speed

        if pressed[pygame.K_DOWN] and y < height - radius - 1:
               y += speed

        if pressed[pygame.K_LEFT] and x > radius + 1: 
               x -= speed

        if pressed[pygame.K_RIGHT] and x < width - radius - 1 : 
               x += speed
        
        screen.fill((255, 255, 255))
        pygame.draw.circle(screen, color, (x, y), radius)
        pygame.display.flip()

        clock.tick(60)

pygame.quit()


